"""
Main Flask application for the Internal Service Request Tracking System.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from config import Config
from database import init_db, insert_request, get_all_requests, update_request_status

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database on startup
init_db()

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
def index():
    """Home page redirect to submit."""
    return redirect(url_for('submit'))

@app.route('/submit', methods=['GET', 'POST'])
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