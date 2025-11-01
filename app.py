"""
Main Flask application for the Internal Service Request Tracking System.
"""
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from database import init_db, init_auth_db, init_settings_db, insert_request, get_all_requests, update_request_status, get_user_by_username, get_setting, update_setting, get_all_settings, get_decrypted_setting

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

# Initialize databases on startup
init_db()
init_auth_db()
init_settings_db()

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login."""
    from database import get_user_by_id
    user_data = get_user_by_id(user_id)
    if user_data:
        # Create a simple user object for Flask-Login
        class User:
            def __init__(self, user_data):
                self.id = user_data['id']
                self.username = user_data['username']
                self.role = user_data['role']
                self.is_active = user_data['is_active']

            @property
            def is_authenticated(self):
                return True

            @property
            def is_anonymous(self):
                return False

            def get_id(self):
                return str(self.id)

        return User(user_data)
    return None

def get_departments():
    """Fetch department data from external API."""
    try:
        response = requests.get(f"{Config.API_BASE_URL}/users")
        if response.status_code == 200:
            users = response.json()
            # Extract unique departments (using company names as departments for demo)
            departments = list(set(user['company']['name'] for user in users))
            return departments
    except Exception as e:
        app.logger.error(f"Error fetching departments: {e}")
    return ['IT Support', 'Human Resources', 'Finance', 'Operations', 'Customer Service']  # Fallback for financial institution

def send_notification_email(requester_name, department, category, description):
    """Send email notification for new service request using SMTP."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_FROM
        msg['To'] = Config.EMAIL_TO
        msg['Subject'] = f'New IT Service Request from {requester_name}'

        email_content = f"""
        New IT Service Request Submitted:

        Requester: {requester_name}
        Department: {department}
        Category: {category}
        Description: {description}

        Please review and resolve this request in the admin panel.
        Login to: https://internal-service-request-tracking-system.onrender.com/
        """

        msg.attach(MIMEText(email_content, 'plain'))

        # Get settings from database (with decryption for sensitive data)
        smtp_server = get_setting('smtp_server') or Config.SMTP_SERVER
        smtp_port = int(get_setting('smtp_port') or Config.SMTP_PORT)
        smtp_username = get_setting('smtp_username') or Config.SMTP_USERNAME
        smtp_password = get_decrypted_setting('smtp_password') or Config.SMTP_PASSWORD
        email_from = get_setting('email_from') or Config.EMAIL_FROM
        email_to = get_setting('email_to') or Config.EMAIL_TO

        # Send email using SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()

        app.logger.info(f"Email notification sent successfully to {Config.EMAIL_TO}")
        return True
    except Exception as e:
        app.logger.error(f"Error sending email notification: {e}")
        # For demo purposes, don't fail the request if email fails
        return False

@app.route('/')
@login_required
def index():
    """Home page redirect based on user role."""
    if current_user.role == 'admin':
        return redirect(url_for('admin'))
    return redirect(url_for('submit'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please provide both username and password.', 'error')
            return redirect(url_for('login'))

        user = get_user_by_username(username)
        if user:
            from werkzeug.security import check_password_hash
            if check_password_hash(user['password_hash'], password):
                # Create a simple user object for Flask-Login
                class User:
                    def __init__(self, user_data):
                        self.id = user_data['id']
                        self.username = user_data['username']
                        self.role = user_data['role']
                        self.is_active = user_data['is_active']

                    @property
                    def is_authenticated(self):
                        return True

                    @property
                    def is_anonymous(self):
                        return False

                    def get_id(self):
                        return str(self.id)

                login_user(User(user))
                flash(f'Welcome back, {username}!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('index'))
        flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    """Handle service request submission."""
    if request.method == 'POST':
        requester_name = request.form.get('requester_name')
        department = request.form.get('department')
        category = request.form.get('category')
        description = request.form.get('description')

        if not all([requester_name, department, category, description]):
            flash('All fields are required.', 'error')
            return redirect(url_for('submit'))

        insert_request(requester_name, department, category, description)

        # Send email notification
        send_notification_email(requester_name, department, category, description)

        flash('Request submitted successfully! IT support has been notified.', 'success')
        return redirect(url_for('submit'))

    departments = get_departments()
    categories = ['Hardware Issue', 'Software Issue', 'Network Problem', 'Access Request', 'Other']
    return render_template('submit.html', departments=departments, categories=categories)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    """Admin panel to view and update requests."""
    if request.method == 'POST':
        # Handle request status updates
        request_id = request.form.get('request_id')
        status = request.form.get('status')
        if request_id and status:
            update_request_status(request_id, status)
            flash('Request status updated successfully!', 'success')
            return redirect(url_for('admin'))

        # Handle settings updates
        setting_key = request.form.get('setting_key')
        setting_value = request.form.get('setting_value')
        if setting_key and setting_value is not None:
            update_setting(setting_key, setting_value)
            flash('Settings updated successfully!', 'success')
            return redirect(url_for('admin'))

    requests_data = get_all_requests()
    settings = get_all_settings()
    return render_template('admin.html', requests=requests_data, settings=settings)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=Config.DEBUG)