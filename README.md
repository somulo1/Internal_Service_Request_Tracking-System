# Internal Service Request Tracking System

A lightweight web-based system built with Flask and SQLite to automate internal IT service requests, replacing manual email handling. The system allows staff to submit, track, and manage IT issues efficiently while providing administrators with tools for monitoring and resolving requests in real time.

## Features

- **Staff Submission**: Submit IT service requests with name, department, category, and description
- **Admin Management**: View all requests and update their status
- **Dynamic Departments**: Pull department data dynamically from external API
- **Status Automation**: Default "Pending" status, auto-update to "Resolved" when marked complete
- **SQLite Storage**: Persistent storage with schema: id, requester_name, department, category, description, status, created_at

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/somulo1/Internal_Service_Request_Tracking-System.git
   cd Internal_Service_Request_Tracking-System
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   - **Live Demo**: https://internal-service-request-tracking-system.onrender.com
   - Local development: http://localhost:5000/login
   - Submit requests: http://localhost:5000/submit (staff only)
   - Admin panel: http://localhost:5000/admin (admin only)

## Usage

### Authentication
**Demo Credentials:**
- **Admin Account**: username: `admin`, password: `admin123`
- **Staff Account**: username: `staff`, password: `staff123`

### Submitting a Request (Staff)
1. Login with staff credentials
2. Navigate to Submit Request
3. Fill in your name, select department and category
4. Provide a detailed description
5. Click "Submit Request"

### Admin Panel (Admin Only)
1. Login with admin credentials
2. View all submitted requests in a table
3. Update request status using dropdown menus
4. Configure email notification settings

## Design Notes

- **Modular Architecture**: Code is organized into separate modules (app.py, database.py, config.py)
- **Clean UI**: Uses Bootstrap for responsive design
- **Error Handling**: Includes flash messages for user feedback
- **Security**: Basic input validation and secure practices
- **Deployment Ready**: Includes Procfile for Render hosting

## Deployment

The application is configured for deployment on Render:

- **Procfile**: `web: gunicorn app:app`
- **Requirements**: Flask, gunicorn, requests
- **Database**: SQLite remains local for demo purposes

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap 5
- **External API**: JSONPlaceholder for department data
- **Deployment**: Gunicorn, Render
