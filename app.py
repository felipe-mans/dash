from flask import Flask
from flask import redirect, render_template, request, session
import time

@app.route('')
@app.route('/home')
def home():
    return render_template('index.html')    

### LOGIN
## taken from David and Alvin's api-project, WeatherText
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = session.get('user', None)
    if user:
        return redirect('/user')
    if request.method == 'GET':
        return render_template('login.html')
    
    # Logs the user in if they are authorized.
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if dbm.is_user_authenticated(username, password):
        session['user'] = username
        return redirect('/user')
    return render_template('login.html',
                           error_message='Invalid credentials. Try again')

### LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

### USER SETTINGS PAGE
@app.route('/user')
def user():
    user = session.get('user', None)
    if not user:
        return render_template('register.html',
                               message='You are not a registered user!')
    userdata = dbm.get_user_by_username(user)
    return render_template('user.html', userdata=userdata)
