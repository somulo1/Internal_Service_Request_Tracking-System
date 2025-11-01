# Changelog

All notable changes to the Internal Service Request Tracking System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-01

### Added
- **Core Application Features**
  - Flask web application with request submission and admin management
  - SQLite database integration with proper schema
  - Bootstrap 5 responsive UI templates
  - External API integration for dynamic department data
  - Status automation (Pending → Resolved workflow)

- **Database Schema**
  - `requests` table with fields: id, requester_name, department, category, description, status, created_at
  - Automatic timestamp generation
  - Default status handling

- **User Interface**
  - Request submission form with validation
  - Admin dashboard with request management
  - Real-time status updates
  - Flash messages for user feedback

- **API Integration**
  - JSONPlaceholder integration for department data
  - Graceful fallback for API failures
  - Error handling and logging

- **Deployment Ready**
  - Procfile for Render deployment
  - Gunicorn WSGI server configuration
  - Environment variable support
  - Production security settings

- **Documentation**
  - Comprehensive README with setup instructions
  - Architecture documentation
  - API reference guide
  - Deployment guide
  - Contributing guidelines
  - Visual diagrams (Mermaid format)

### Technical Details
- **Backend**: Python Flask framework
- **Database**: SQLite with proper connection handling
- **Frontend**: HTML5, Bootstrap 5, Jinja2 templates
- **External Services**: JSONPlaceholder API
- **Deployment**: Render with Gunicorn

### Security
- Input validation and sanitization
- SQL injection prevention via parameterized queries
- Secure default configurations
- Environment variable usage for sensitive data

### Performance
- Efficient database queries
- Bootstrap CDN for fast loading
- Minimal external dependencies
- Optimized for small to medium organizations

## Types of Changes
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities

## Development Status
This is the initial release (v1.0.0) of the Internal Service Request Tracking System. The application is production-ready and includes all core features required for IT service request management.

Future releases will focus on:
- User authentication system
- Advanced filtering and search
- Email notifications
- File attachments
- REST API endpoints
- Mobile responsiveness improvements