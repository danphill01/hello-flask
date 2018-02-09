from flask import Flask, request, redirect, render_template
import cgi
import os
#import jinja2

#we don't need this if we use render_template from Flask module, 
#  we pull from the 'templates' dir and use autoescape
#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja2 config
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

#Create the app object from the Flask constructor
app = Flask(__name__)
#the DEBUG configuration setting for the Flask application will be enabled. This enables some behaviors that are helpful when developing Flask apps, such as displaying errors in the browser, and ensuring file changes are reloaded while the server is running (aka "host swapping")
app.config['DEBUG'] = True


#decorator that maps root path "/" to function
@app.route("/")
def index():
    #this is the original way to do template rendering
    #template = jinja_env.get_template('hello_form.html')
    #return template.render()
    #but since we set up jinja_env to know where templates are,  
    #now we import render_template from Flask and use the shorthand
    return render_template('hello_form.html')

#a new route to handle the form submission as a post request
@app.route("/hello", methods=['POST'])
def hello():
    #retrieve the data from the form object (like a dictionary)
    first_name = request.form['first_name']
    return render_template('hello_greeting.html', name=first_name)


@app.route('/validate-time')
def display_time_form():
    return render_template('time_form.html')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        return render_template('time_form.html', hours_error=hours_error,
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)


tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="TODOs", tasks=tasks)


#run the app
app.run()
