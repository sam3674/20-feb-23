import sqlite3
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
    def add_task(self, task_name, start_time, end_time):
        if start_time >= end_time:
            print("Error: Invalid start and end time")
            return
        try:
            self.cursor.execute("""
                INSERT INTO schedule (task_name, start_time, end_time)
                VALUES (?, ?, ?)
            """, (task_name, start_time, end_time))
            self.conn.commit()
            print("Task added successfully")
        except sqlite3.IntegrityError:
            print("Error: Task already exists at this time")
    def remove_task(self, start_time):
        self.cursor.execute("""
            DELETE FROM schedule
            WHERE start_time=?
        """, (start_time,))
        self.conn.commit()
        if self.cursor.rowcount == 0:
            print("Error: Task not found")
        else:
            print("Task removed successfully")
    def view_schedule(self):
        self.cursor.execute("""
            SELECT task_name, start_time, end_time
            FROM schedule
            ORDER BY start_time
        """)
        schedule = self.cursor.fetchall()
        if not schedule:
            print("No tasks scheduled")
            return
        print("Task Name\tStart Time\tEnd Time")
        for task_name, start_time, end_time in schedule:
            print("{}\t\t{}\t\t{}".format(task_name, start_time, end_time))
    def get_tasks(self):
        self.cursor.execute("""
            SELECT task_name, start_time, end_time
            FROM schedule
            ORDER BY start_time
        """)
        tasks = self.cursor.fetchall()
        return tasks
            
#schedule = Schedule()
#schedule.add_task("Meeting with John", 10, 11)
#schedule.add_task("Call with Jane", 11, 12)
#schedule.view_schedule()
#schedule.remove_task(11)
#schedule.view_schedule()