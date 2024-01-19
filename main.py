import sqlite3
import Faker
import random

fake = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT,
        group_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        group_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        teacher_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    )
''')


group_names = ['Group A', 'Group B', 'Group C']
for group_name in group_names:
    cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group_name,))

for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute('INSERT INTO students (student_name, group_id) VALUES (?, ?)', (student_name, group_id))

for _ in range(3):
    teacher_name = fake.name()
    cursor.execute('INSERT INTO teachers (teacher_name) VALUES (?)', (teacher_name,))

subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science', 'Art']
for subject_name in subject_names:
    teacher_id = random.randint(1, 3)
    cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject_name, teacher_id))

for student_id in range(1, 31):
    for subject_id in range(1, 9):
        grade = random.randint(60, 100)
        date_received = fake.date_this_decade()
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, grade, date_received))


conn.commit()
conn.close()
