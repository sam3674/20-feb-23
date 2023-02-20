from flask import Flask, request, render_template

app = Flask(__name__)

##Define a route: You can define a route in Flask using the `route` decorator. Here's an example:
@app.route("/")
def homepage():
    return render_template("homepage.html")

## Render a template: You can render a template in Flask using the `render_template` function. Here's an example:
@app.route("/schedule")
def schedule():
    #tasks = get_tasks()
    return render_template("schedule.html")#, tasks=tasks) 


if __name__=='__main__':
    app.run(debug=True, use_debugger=False, use_reloader=True)
##In this example, a route is defined for the `/schedule` URL, and the `render_template` function is used to render a template named `schedule.html` with a list of tasks as a parameter.


##Create the template: You can create the template in a separate file in the `templates` directory. Here's an example:


## Run the application: You can run the application using the following command:
#flask run
#The `flask run` command is used to start the Flask development server, and the scheduling app can be accessed in a web browser at `http://localhost:5000/`.
