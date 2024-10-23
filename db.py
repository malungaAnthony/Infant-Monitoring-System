import sqlite3

def create_database():
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('hospital_database.db')  # You can change the name if you want
    cursor = conn.cursor()

    # Create the Baby_QR_Codes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Baby_QR_Codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baby_id TEXT NOT NULL,
            parent_id TEXT NOT NULL,
            hospital_id TEXT NOT NULL,
            qr_code_image_path TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_database()

