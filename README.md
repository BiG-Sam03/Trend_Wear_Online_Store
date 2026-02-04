
# Trend Wear Online Store

A simple Python project for login and registration using MySQL database.

## Requirements

- Python 3.x
- MySQL server

## How to run

1. Create a database with the following structure in MySQL:
   ```sql
   CREATE DATABASE IF NOT EXISTS online_shop;
   USE online_shop;
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(100) NOT NULL,
       password VARCHAR(100) NOT NULL
   );
   ```

2. Install required packages:
   ```bash
   pip install mysql-connector
   ```

3. Run the application:
   ```bash
   python login.py
   python register.py
   ```

## License

This project is licensed under the MIT License.
