"""
Database module for managing SQLite operations in the Internal Service Request Tracking System.
"""

import sqlite3
from datetime import datetime
from config import Config

def get_db_connection():
    """Establish and return a database connection."""
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the required schema."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requester_name TEXT NOT NULL,
            department TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_request(requester_name, department, category, description):
    """Insert a new service request into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO requests (requester_name, department, category, description)
        VALUES (?, ?, ?, ?)
    ''', (requester_name, department, category, description))
    conn.commit()
    conn.close()

def get_all_requests():
    """Retrieve all service requests from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM requests ORDER BY created_at DESC')
    requests = cursor.fetchall()
    conn.close()
    return requests

def update_request_status(request_id, status):
    """Update the status of a specific request."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE requests SET status = ? WHERE id = ?
    ''', (status, request_id))
    conn.commit()
    conn.close()

def init_auth_db():
    """Initialize authentication database tables."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create users table for authentication
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'staff',
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create default admin user if not exists
    cursor.execute('SELECT id FROM users WHERE username = ?', ('admin',))
    if not cursor.fetchone():
        from werkzeug.security import generate_password_hash
        hashed_admin_password = generate_password_hash('admin123')
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        ''', ('admin', 'admin@company.com', hashed_admin_password, 'admin'))

    # Create default staff user
    cursor.execute('SELECT id FROM users WHERE username = ?', ('staff',))
    if not cursor.fetchone():
        from werkzeug.security import generate_password_hash
        hashed_staff_password = generate_password_hash('staff123')
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        ''', ('staff', 'staff@company.com', hashed_staff_password, 'staff'))

    conn.commit()
    conn.close()

def get_user_by_username(username):
    """Get user by username for authentication."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND is_active = 1', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    """Get user by ID for Flask-Login."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ? AND is_active = 1', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def init_settings_db():
    """Initialize settings table for configurable options."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create settings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            description TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert default email settings
    default_settings = [
        ('smtp_server', 'smtp.gmail.com', 'SMTP server hostname'),
        ('smtp_port', '587', 'SMTP server port'),
        ('smtp_username', 'mcomulosammy37@gmail.com', 'SMTP username'),
        ('smtp_password', 'eptw taih ilqn srls', 'SMTP password'),
        ('email_from', 'mcomulosammy37@gmail.com', 'From email address'),
        ('email_to', 'mcomulosammy37@gmail.com', 'To email address'),
        ('email_notifications', 'true', 'Enable email notifications')
    ]

    for key, value, description in default_settings:
        cursor.execute('''
            INSERT OR IGNORE INTO settings (key, value, description)
            VALUES (?, ?, ?)
        ''', (key, value, description))

    conn.commit()
    conn.close()

def get_setting(key):
    """Get a setting value by key."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
    result = cursor.fetchone()
    conn.close()
    return result['value'] if result else None

def update_setting(key, value):
    """Update a setting value with encryption for sensitive data."""
    from cryptography.fernet import Fernet
    import base64

    # Encrypt sensitive settings
    sensitive_keys = ['smtp_password']
    if key in sensitive_keys and value:
        # Use a simple key for demo (in production, use environment variable)
        key_fernet = base64.urlsafe_b64encode(b'secure_key_for_demo_only_not_for_prod')
        f = Fernet(key_fernet)
        value = f.encrypt(value.encode()).decode()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE settings SET value = ?, updated_at = CURRENT_TIMESTAMP
        WHERE key = ?
    ''', (value, key))
    conn.commit()
    conn.close()

def get_decrypted_setting(key):
    """Get a setting value with decryption for sensitive data."""
    from cryptography.fernet import Fernet
    import base64

    value = get_setting(key)
    if not value:
        return None

    # Decrypt sensitive settings
    sensitive_keys = ['smtp_password']
    if key in sensitive_keys:
        try:
            key_fernet = base64.urlsafe_b64encode(b'secure_key_for_demo_only_not_for_prod')
            f = Fernet(key_fernet)
            value = f.decrypt(value.encode()).decode()
        except:
            # If decryption fails, return empty string
            return ""

    return value

def get_all_settings():
    """Get all settings for admin configuration."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM settings ORDER BY key')
    settings = cursor.fetchall()
    conn.close()
    return settings