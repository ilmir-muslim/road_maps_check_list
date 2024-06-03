import sqlite3
import json


def create_db():
    conn = sqlite3.connect('data_tests/data.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS members
        (user_id primary key, name text, added_date text, studying_day integer, studying_stage text)""")

    c.execute("""CREATE TABLE IF NOT EXISTS road_map
        (current_progress primary key, studying_stage text)""")

    conn.commit()
    conn.close()


def transfer_data():
    with open('data_tests/road_map.json', 'r') as file:
        road_map = json.load(file)

    conn = sqlite3.connect('data_tests/data.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS road_map (current_progress INTEGER PRIMARY KEY, studying_stage TEXT)')

    for key, value in road_map.items():
        current_progress = int(key)
        studying_stage = value
        c.execute("INSERT INTO road_map (current_progress, studying_stage) VALUES (?, ?)",
                  (current_progress, studying_stage))

    conn.commit()
    conn.close()


def print_road_map():
    conn = sqlite3.connect('data_tests/data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM road_map')
    road_map = c.fetchall()

    print('Таблица road_map:')
    print('---------------')
    print('current_progress | studying_stage')
    print('-------------------------------')
    for row in road_map:
        current_progress = row[0]
        studying_stage = row[1]
        print(f'{current_progress} | {studying_stage}')

    conn.close()


def get_all_student_data():
    conn = sqlite3.connect('data_tests/data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    student_data = []
    for row in rows:
        user_id, name, join_date, current_progress, studying_stage = row
        student_data.append({
            'user_id': user_id,
            'name': name,
            'join_date': join_date,
            'current_progress': current_progress,
            'studying_stage': studying_stage
        })

    return student_data


def get_road_map():
    conn = sqlite3.connect('data_tests/data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM road_map")
    rows = cursor.fetchall()

    road_map = []
    for row in rows:
        current_progress, studying_stage = row
        road_map.append({
            'current_progress': current_progress,
            'studying_stage': studying_stage
        })

    return road_map


with open('messages.html', 'r', encoding='utf-8') as file:
    result = file.read()
print(result)
