"""
Main Flask application for the Internal Service Request Tracking System.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
import requests
from config import Config
from database import init_db, init_auth_db, insert_request, get_all_requests, update_request_status, get_user_by_username

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
    return ['IT', 'HR', 'Finance', 'Operations']  # Fallback

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
        if user and user['password_hash'] == password:  # Simple check for demo
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
        else:
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
        flash('Request submitted successfully!', 'success')
        return redirect(url_for('submit'))

    departments = get_departments()
    categories = ['Hardware Issue', 'Software Issue', 'Network Problem', 'Access Request', 'Other']
    return render_template('submit.html', departments=departments, categories=categories)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    """Admin panel to view and update requests."""
    if request.method == 'POST':
        request_id = request.form.get('request_id')
        status = request.form.get('status')
        if request_id and status:
            update_request_status(request_id, status)
            flash('Request status updated successfully!', 'success')
        return redirect(url_for('admin'))

    requests_data = get_all_requests()
    return render_template('admin.html', requests=requests_data)

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)