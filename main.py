from flask import Flask, request

#Create the app object from the Flask constructor
app = Flask(__name__)
#the DEBUG configuration setting for the Flask application will be enabled. This enables some behaviors that are helpful when developing Flask apps, such as displaying errors in the browser, and ensuring file changes are reloaded while the server is running (aka "host swapping")
app.config['DEBUG'] = True

#form string in main.py for now, will put into a template later
form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

#decorator that maps root path "/" to function
@app.route("/")
def index():
    return form

#a new route to handle the form submission as a post request
@app.route("/hello", methods=['POST'])
def hello():
    #retrieve the data from the form object (like a dictionary)
    first_name = request.form['first_name']
    #return the HTML for the browser to render
    return '<h1>Hello, ' + first_name + '</h1>'

#run the app
app.run()
