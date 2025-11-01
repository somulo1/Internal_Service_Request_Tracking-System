# Internal Service Request Tracking System

A comprehensive web-based system built with Flask and SQLite to automate internal IT service requests, featuring user authentication, email notifications, and admin dashboard functionality.

## Features

- **User Authentication**: Secure login system with role-based access (admin/staff)
- **Staff Submission**: Submit IT service requests with name, department, category, and description
- **Admin Management**: View all requests, update status, and configure system settings
- **Email Notifications**: Automated SMTP notifications for new service requests
- **Dynamic Departments**: Pull department data from external API with fallback options
- **Status Automation**: Default "Pending" status with admin-controlled updates
- **SQLite Storage**: Persistent storage with complete schema

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

- **Modular Architecture**: Code organized into separate modules (app.py, database.py, config.py)
- **Security**: Password hashing, encrypted SMTP credentials, role-based access control
- **Clean UI**: Bootstrap 5 responsive design with consistent green theming
- **Error Handling**: Flash messages for user feedback and validation
- **Deployment Ready**: Includes Procfile for Render hosting

## Deployment

The application is configured for deployment on Render:

- **Procfile**: `web: gunicorn app:app`
- **Requirements**: Flask, gunicorn, requests, Flask-Login, Werkzeug
- **Database**: SQLite remains local for demo purposes
- **Environment Variables**: Configure SMTP settings via environment variables

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Authentication**: Flask-Login
- **Security**: Werkzeug (password hashing)
- **Frontend**: HTML, Bootstrap 5
- **Email**: smtplib with SMTP
- **External API**: JSONPlaceholder for department data
- **Deployment**: Gunicorn, Render

## Documentation

For detailed technical documentation, see the [docs/](docs/) directory:

- **[Architecture Overview](docs/ARCHITECTURE.md)**: System design and technology stack
- **[API Reference](docs/API_REFERENCE.md)**: Complete API documentation
- **[Deployment Guide](docs/DEPLOYMENT.md)**: Setup and deployment instructions
- **[Contributing Guidelines](docs/CONTRIBUTING.md)**: Development workflow and standards

### Visual Diagrams

- **[System Architecture](docs/system_architecture.mmd)**: Mermaid diagram of system components
- **[Database Schema](docs/database_schema.mmd)**: Entity relationship diagram
- **[User Flow](docs/user_flow.mmd)**: User interaction flowchart

### Additional Documentation

- **[Changelog](docs/CHANGELOG.md)**: Version history and release notes

## Project Structure

```
Internal_Service_Request_Tracking-System/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── database.py           # Database operations
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── LICENSE              # MIT License
├── README.md            # Project documentation
├── requests.db          # SQLite database file
├── templates/           # Jinja2 templates
│   ├── base.html        # Base template with Bootstrap
│   ├── submit.html      # Request submission form
│   └── admin.html       # Admin dashboard
├── static/              # Static assets (reserved for future use)
└── docs/                # Technical documentation
    ├── ARCHITECTURE.md
    ├── API_REFERENCE.md
    ├── DEPLOYMENT.md
    ├── CONTRIBUTING.md
    ├── system_architecture.mmd
    ├── database_schema.mmd
    └── user_flow.mmd
```
