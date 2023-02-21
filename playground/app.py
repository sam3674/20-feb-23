from flask import Flask, request, render_template
#import aSqlite.py
import sqlite3
app = Flask(__name__)

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

##Define a route: You can define a route in Flask using the `route` decorator. Here's an example:
@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/schedule")
def schedule():
    tasks = get_tasks()
    print('line30')
    return render_template("schedule.html", tasks=tasks)

if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')#,debug=True, use_debugger=False, use_reloader=True)
