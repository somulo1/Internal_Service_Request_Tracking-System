# API Reference

## Internal Routes

### GET /
**Redirect to submission form**
- **Purpose**: Entry point for the application
- **Response**: Redirects to `/submit`

### GET/POST /submit
**Service request submission**
- **GET**: Display submission form
- **POST**: Process form submission
- **Parameters** (POST):
  - `requester_name` (string, required): Name of the requester
  - `department` (string, required): Department selection
  - `category` (string, required): Issue category
  - `description` (string, required): Issue description
- **Response**: Success/error messages with form

### GET/POST /admin
**Admin dashboard**
- **GET**: Display all service requests
- **POST**: Update request status
- **Parameters** (POST):
  - `request_id` (integer, required): ID of request to update
  - `status` (string, required): New status (Pending/In Progress/Resolved)
- **Response**: Updated request list

## External API Dependencies

### JSONPlaceholder Users API
**URL**: `https://jsonplaceholder.typicode.com/users`
**Method**: GET
**Purpose**: Fetch department data for form population
**Response Format**:
```json
[
  {
    "id": 1,
    "name": "Samuel Omulo",
    "company": {
      "name": "kisumu-based"
    }
  }
]
```
**Usage**: Company names are extracted as department options

## Database Functions

### init_db()
**Initialize database schema**
- Creates `requests` table if it doesn't exist
- Sets up proper column structure

### get_db_connection()
**Establish database connection**
- Returns SQLite connection with row factory
- Handles connection management

### insert_request(name, dept, category, desc)
**Insert new service request**
- Parameters: requester_name, department, category, description
- Auto-generates ID and timestamp

### get_all_requests()
**Retrieve all requests**
- Returns list of all service requests
- Ordered by creation date (newest first)

### update_request_status(id, status)
**Update request status**
- Parameters: request_id, new_status
- Updates existing request record

## Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key (defaults to dev key)
- `FLASK_DEBUG`: Debug mode (true/false)
- `DATABASE`: SQLite database path

### Default Settings
- Database: `requests.db` in project root
- Debug: False in production
- API Base: JSONPlaceholder

## Error Handling

### Form Validation
- All fields required
- Server-side validation
- User-friendly error messages

### API Failures
- Graceful fallback for department data
- Static department list as backup
- Error logging for debugging

### Database Errors
- Connection handling
- Transaction safety
- User feedback on failures

## Response Codes

- **200**: Successful request
- **302**: Redirect after form submission
- **404**: Route not found
- **500**: Server error

## Data Formats

### Request Data Structure
```python
{
    'id': 1,
    'requester_name': 'John Doe',
    'department': 'IT',
    'category': 'Hardware Issue',
    'description': 'Computer not starting',
    'status': 'Pending',
    'created_at': '2025-01-01 10:00:00'
}
```

### Form Categories
- Hardware Issue
- Software Issue
- Network Problem
- Access Request
- Other

### Status Values
- Pending (default)
- In Progress
- Resolved