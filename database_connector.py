import sqlite3

DATABASE_NAME = 'data.db'

def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_db_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            student_group TEXT NOT NULL,
            gpa REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# C - Create
def insert_item(first_name, last_name, student_group, gpa):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, student_group, gpa)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, student_group, gpa))
    conn.commit()
    conn.close()

# R - Read All
def get_all_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students ORDER BY id DESC')
    items = cursor.fetchall()
    conn.close()
    return items

# R - Read One
def get_item_by_id(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item

# U - Update
def update_item(item_id, first_name, last_name, student_group, gpa):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET first_name = ?, last_name = ?, student_group = ?, gpa = ?
        WHERE id = ?
    ''', (first_name, last_name, student_group, gpa, item_id))
    conn.commit()
    conn.close()

# D - Delete
def delete_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()