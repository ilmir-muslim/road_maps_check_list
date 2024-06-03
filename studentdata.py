import datetime
import sqlite3


class StudentData:
    def __init__(self):
        self.conn = sqlite3.connect('data_tests/data.db')
        self.cursor = self.conn.cursor()

    def add_data_to_db(self, user_id, name: str, added_date: str):
        self.cursor.execute("INSERT INTO members VALUES (?, ?, ?, ?, ?)",
                            (user_id, name, added_date, 1, 1))
        self.conn.commit()

    # Получение всех данных о студентах из базы данных
    def get_user_id(self):
        self.cursor.execute("SELECT user_id FROM members")
        result = self.cursor.fetchall()
        list_of_tuples = result
        ids = [item[0] for item in list_of_tuples]
        print(ids)
        return ids

    def get_added_date(self, user_id):
        self.cursor.execute("SELECT added_date FROM members WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchall()
        return result[0][0]

    def get_current_progress(self, user_id):
        self.cursor.execute("SELECT current_progress FROM members WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchall()
        return result[0][0]

    def get_studying_stage(self, user_id):
        self.cursor.execute("SELECT studying_stage FROM members WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchall()
        return result[0][0]

    def next_stage(self, current_progress):
        self.cursor.execute('SELECT studying_stage FROM road_map WHERE current_progress = ?',
                            (current_progress + 1,))
        next_stage = self.cursor.fetchall()
        return next_stage[0][0]

    def previous_stage(self, current_progress):
        self.cursor.execute('SELECT studying_stage FROM road_map WHERE current_progress = ?',
                            (current_progress - 1,))
        previous_stage = self.cursor.fetchall()
        return previous_stage[0][0]

    # Удаление данных о студенте из базы данных
    @staticmethod
    def delete_student_data(name):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        c.execute("DELETE FROM members WHERE name = ?", (name,))

        conn.commit()
        conn.close()

    def studying_days(self, user_id):
        join_date = self.get_added_date(user_id)
        current_date = datetime.datetime.now()
        days = (current_date - join_date).days
        return days
