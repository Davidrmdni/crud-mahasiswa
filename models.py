from database import get_db

def add_student(name, age, major):
    with get_db() as conn:
        conn.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))

def get_students():
    with get_db() as conn:
        return conn.execute("SELECT * FROM students").fetchall()

def update_student(student_id, name, age, major):
    with get_db() as conn:
        conn.execute("UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?", (name, age, major, student_id))

def delete_student(student_id):
    with get_db() as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
