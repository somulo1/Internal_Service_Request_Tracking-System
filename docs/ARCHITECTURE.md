# Architecture Documentation

## System Overview

The Internal Service Request Tracking System is a Flask-based web application designed to streamline IT service request management within organizations. The system provides a clean interface for staff to submit requests and administrators to manage them efficiently.

## Technology Stack

- **Backend**: Python Flask framework
- **Database**: SQLite for persistent storage
- **Frontend**: HTML5, Bootstrap 5, Jinja2 templates
- **External APIs**: JSONPlaceholder for department data
- **Deployment**: Gunicorn, Render hosting

## Application Structure

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
└── static/              # Static assets (currently empty)
```

## Database Schema

### requests Table

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Auto-incrementing unique identifier |
| requester_name | TEXT | Name of the person submitting the request |
| department | TEXT | Department the requester belongs to |
| category | TEXT | Type of IT issue (Hardware, Software, Network, etc.) |
| description | TEXT | Detailed description of the issue |
| status | TEXT | Current status (Pending, In Progress, Resolved) |
| created_at | TIMESTAMP | Automatic timestamp of request creation |

## API Endpoints

### Web Routes

- `GET /` - Redirects to submission form
- `GET/POST /submit` - Service request submission form
- `GET/POST /admin` - Admin dashboard for managing requests

### External API Integration

- **JSONPlaceholder Users API**: `https://jsonplaceholder.typicode.com/users`
  - Used to dynamically fetch department data
  - Fallback to static list if API unavailable

## Data Flow

1. **Request Submission**:
   - User fills form on `/submit`
   - Data validated and stored in SQLite
   - Success message displayed

2. **Admin Management**:
   - Admin views all requests on `/admin`
   - Can update request status via dropdown
   - Changes saved to database

3. **Department Data**:
   - Fetched from external API on form load
   - Cached for performance
   - Graceful fallback if API fails

## Security Considerations

- Input validation on all form fields
- SQL injection prevention via parameterized queries
- No sensitive data stored in plain text
- Environment variables for configuration
- Secure defaults for production deployment

## Deployment Architecture

### Local Development
- Run with `python app.py`
- Debug mode enabled
- Local SQLite database

### Production (Render)
- Gunicorn WSGI server
- Environment variables for configuration
- SQLite database included in repo for demo

## Performance Optimizations

- Database connection pooling
- Minimal external dependencies
- Bootstrap CDN for fast loading
- Efficient SQL queries with proper indexing

## Future Enhancements

- User authentication system
- Email notifications
- Advanced filtering and search
- Request priority levels
- File attachments
- REST API endpoints
- Database migration system