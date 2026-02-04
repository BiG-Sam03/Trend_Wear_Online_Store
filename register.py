
from db import connect_to_database

# Function to register a new user
def register_user(username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    # Insert the new user into the users table
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()  # Save the changes
    conn.close()
    
    print("Registration successful!")
