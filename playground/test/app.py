from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_checkbox():
    data = request.form['data']


    
    checkbox_value = request.form.get('checkbox')
    if checkbox_value:
            # Checkbox is checked
            # Do something with the data
            return f"Data: {data} (checkbox is checked)"
    else:
             # Checkbox is not checked
             # Do something else with the data
         return f"Data: {data} (checkbox is not checked)"


@app.route('/', methods=['POST','GET'])
def about_page():   
    return render_template("test.html")

app.run(debug=True)