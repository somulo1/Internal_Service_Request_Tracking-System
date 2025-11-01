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
        # Note: In production, use proper password hashing
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        ''', ('admin', 'admin@company.com', 'admin123', 'admin'))

    # Create default staff user
    cursor.execute('SELECT id FROM users WHERE username = ?', ('staff',))
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        ''', ('staff', 'staff@company.com', 'staff123', 'staff'))

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