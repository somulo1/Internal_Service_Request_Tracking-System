"""
Configuration settings for the Internal Service Request Tracking System.
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE = os.path.join(os.path.dirname(__file__), 'requests.db')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    API_BASE_URL = 'https://jsonplaceholder.typicode.com'  # Mock API for departments