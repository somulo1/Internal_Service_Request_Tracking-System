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
   - Submit requests: http://localhost:5000/submit
   - Admin panel: http://localhost:5000/admin

## Usage

### Submitting a Request
1. Navigate to `/submit`
2. Fill in your name, select department and category
3. Provide a detailed description
4. Click "Submit Request"

### Admin Panel
1. Navigate to `/admin`
2. View all submitted requests in a table
3. Update request status using the dropdown and "Update" button

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
