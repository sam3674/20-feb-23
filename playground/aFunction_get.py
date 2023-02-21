
import sqlite3

conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()



def get_tasks():
            conn = sqlite3.connect("schedule.db")
            cursor = conn.cursor()
            cursor.execute("""
            SELECT task_name, start_time, end_time
            FROM schedule
            ORDER BY start_time
        """)
            tasks = cursor.fetchall()
            return tasks

class Schedule:
    def __init__(self):
        self.conn = sqlite3.connect("schedule.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedule (
                task_name TEXT,
                start_time INTEGER,
                end_time INTEGER
            )
        """)
        self.conn.commit()
    def get_tasks(self):
        self.cursor.execute("""
            SELECT task_name, start_time, end_time
            FROM schedule
            ORDER BY start_time
        """)
        tasks = self.cursor.fetchall()
        return tasks