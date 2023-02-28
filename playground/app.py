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

# @app.route("/schedule",methods = ['get','post'] )
# def schedule(): 
#     schedule = Schedule()
#     tasks = schedule.get_tasks()
#     form = AddNewTaskForm()
#     #schedule.view_schedule()
#     if form.validate_on_submit():
#         if form.user_add.data:
#             flash(f'tasks : {form.AskTaskName.data}, added!')
#             schedule.add_task(f"{form.AskTaskName.data}",form.AskStartTime.data,form.AskEndTime.data)
#         if form.user_delete.data:
#             flash(f'tasks : {form.AskTaskName.data}, deleted!')
#             schedule.remove_task(form.AskTaskName.data)
#         return redirect(url_for('schedule'))
#     return render_template("schedule.html", tasks=tasks,form=form)

 
# #for testing used 
@app.route("/testingCheckbox",methods = ['GET','POST'] )
def testingCheckbox(): #########
    schedule = Schedule()
    tasks = enumerate(schedule.get_tasks())
    aform = AddNewTaskForm()
    #schedule.view_schedule()
   
    if aform.validate_on_submit():   
        
        # if checkbox_value:
        #    aform.AskTaskName.data=str(tasks[0][0])
        #    aform.AskStartTime.data= int(tasks[0][1])

        if aform.user_add.data:
            flash(f'tasks : {aform.AskTaskName.data}, added!')
            schedule.add_task(f"{aform.AskTaskName.data}",aform.AskStartTime.data,aform.AskEndTime.data)
        if aform.user_delete.data:
            flash(f'tasks : {aform.AskTaskName.data}, deleted!')
            schedule.remove_task(aform.AskTaskName.data,aform.AskStartTime.data)
        return redirect(url_for('testingCheckbox'))
                            #############
    return render_template("testingCheckbox.html", tasks=tasks,form=aform)

# @app.route('/process_form', methods=['POST'])
# def process_form():
#     checkbox_value = request.form.get('checkbox_name')
#     if checkbox_value:
#         form.AskTaskName.data=str(tasks[0][0])
#         form.AskStartTime.data= int(tasks[0][1])
#     else:
#         # Checkbox is not checked
#         # Do something else...


if __name__=='__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')#,debug=True, use_debugger=False, use_reloader=True)
