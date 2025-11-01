"""
Configuration settings for the Internal Service Request Tracking System.
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE = os.path.join(os.path.dirname(__file__), 'requests.db')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    API_BASE_URL = 'https://jsonplaceholder.typicode.com'  # Mock API for departments

    # Email configuration (for demo purposes - use environment variables in production)
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME', 'mcomulosammy37@gmail.com')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', 'eptw taih ilqn srls') # strictly use a google generated password. do not use your real password
    EMAIL_FROM = os.environ.get('EMAIL_FROM', 'mcomulosammy37@gmail.com')
    EMAIL_TO = os.environ.get('EMAIL_TO', 'mcomulosammy37@gmail.com')