import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",  # هذا هو عنوان الخادم الافتراضي على جهازك
        user="root",       # افتراضيًا "root" هو اسم المستخدم في XAMPP
        password="",       # افتراضيًا لا يوجد كلمة مرور في XAMPP
        database="online_shop"  # تأكد من أن هذا هو اسم قاعدة البيانات
    )
