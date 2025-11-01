# Deployment Guide

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/somulo1/Internal_Service_Request_Tracking-System.git
   cd Internal_Service_Request_Tracking-System
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open browser to `http://localhost:5000`
   - Submit requests at `/submit`
   - Admin panel at `/admin`

## Production Deployment on Render

### Prerequisites
- Render account
- GitHub repository

### Deployment Steps

1. **Connect Repository**:
   - Go to Render Dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**:
   - **Name**: `internal-service-requests`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

3. **Environment Variables** (Optional):
   - `SECRET_KEY`: Your secret key for production
   - `FLASK_DEBUG`: `false`

4. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Access your live application

## Alternative Deployment Options

### Heroku Deployment

1. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

2. **Set buildpacks**:
   ```bash
   heroku buildpacks:set heroku/python
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

### Docker Deployment

1. **Create Dockerfile**:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   CMD ["gunicorn", "app:app"]
   ```

2. **Build and run**:
   ```bash
   docker build -t service-requests .
   docker run -p 8000:8000 service-requests
   ```

## Database Configuration

### Local Development
- SQLite database (`requests.db`) is created automatically
- Database file is committed to repository for demo purposes

### Production Considerations
- For production, consider using PostgreSQL or MySQL
- Implement database migrations
- Use environment variables for database URLs
- Set up database backups

## Environment Variables

### Required Variables
```bash
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=false
```

### Optional Variables
```bash
DATABASE_URL=sqlite:///requests.db  # For production databases
API_BASE_URL=https://jsonplaceholder.typicode.com
```

## Security Checklist

### Before Deployment
- [ ] Change default SECRET_KEY
- [ ] Set FLASK_DEBUG=false
- [ ] Review database permissions
- [ ] Check file upload restrictions (if added later)
- [ ] Verify HTTPS is enabled
- [ ] Test all forms and functionality

### Production Security
- [ ] Use strong SECRET_KEY
- [ ] Implement rate limiting
- [ ] Add input sanitization
- [ ] Set up monitoring and logging
- [ ] Regular security updates

## Monitoring and Maintenance

### Health Checks
- Application responds to root requests
- Database connections are healthy
- External API dependencies are accessible

### Logs
- Check application logs for errors
- Monitor database performance
- Track user activity patterns

### Updates
- Keep dependencies updated
- Monitor for security vulnerabilities
- Plan regular maintenance windows

## Troubleshooting

### Common Issues

**Application won't start**:
- Check Python version compatibility
- Verify all dependencies are installed
- Check environment variables

**Database errors**:
- Ensure database file permissions
- Check SQLite version
- Verify database schema

**External API failures**:
- Check internet connectivity
- Verify API endpoints
- Review fallback mechanisms

**Deployment failures**:
- Check build logs
- Verify Procfile syntax
- Confirm environment variables

## Performance Optimization

### Database
- Add indexes for frequently queried columns
- Implement connection pooling
- Consider read replicas for high traffic

### Application
- Enable gzip compression
- Use CDN for static assets
- Implement caching where appropriate

### Scaling
- Consider load balancing for high traffic
- Implement database connection pooling
- Monitor resource usage

## Backup and Recovery

### Database Backups
```bash
# SQLite backup
sqlite3 requests.db ".backup 'backup.db'"
```

### Code Repository
- Keep regular commits
- Use feature branches
- Tag releases

### Configuration
- Document all environment variables
- Keep configuration files versioned
- Use secrets management for sensitive data