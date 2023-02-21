from flask import Flask, request, render_template
from aFunction_get import*

schedule = Schedule()
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/schedule")
def schedule():
    tasks = get_tasks()
   
    return render_template("schedule.html", tasks=tasks)
if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')#,debug=True, use_debugger=False, use_reloader=True)
