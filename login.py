
import sqlite3

# Function to validate user login credentials
def validate_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Query to check if the user exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return True  # Login successful
    else:
        return False  # Invalid credentials
