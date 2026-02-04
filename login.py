
import mysql.connector

# Function to validate user login credentials
def validate_user(username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    # Query to check if the user exists in the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return True  # Login successful
    else:
        return False  # Invalid credentials
