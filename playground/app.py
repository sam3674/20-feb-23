from flask import Flask, request, render_template,flash,redirect,url_for
import os
#from flask_sqlalchemy import SQLAlchemy
from bsql import Schedule
from forms import AddNewTaskForm




app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/")
def homepage():
    return render_template("homepage.html")




@app.route("/schedule",methods = ['get','post'] )
def schedule(): 
    schedule = Schedule()
    tasks = schedule.get_tasks()
    form = AddNewTaskForm()
    #schedule.view_schedule()

    if form.validate_on_submit():
        if form.user_add.data:
            flash(f'tasks : {form.AskTaskName.data}, added!')
            schedule.add_task
            (f"{form.AskTaskName.data}",form.AskStartTime.data,form.AskEndTime.data)
        if form.user_delete.data:
            flash(f'tasks : {form.AskTaskName.data}, deleted!')
            schedule.remove_task(form.AskStartTime.data)
        return redirect(url_for('schedule'))
    return render_template("schedule.html", tasks=tasks,form=form)





if __name__=='__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')#,debug=True, use_debugger=False, use_reloader=True)
