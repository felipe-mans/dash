from flask import Flask
from flask import redirect, render_template, request, session
import time

app = Flask(__name__)


@app.route('/')
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
    if authenticate(username, password):
        session['user'] = username
        return redirect('/user')
    return render_template('login.html',
                           error_message='Invalid credentials. Try again')

### LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

### REGISTER
## From David and Alvin's api-project

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')

  username = request.form.get('username', '')
  password = request.form.get('password', '')
  confirm_password = request.form.get('confirm_password', '')
  # mail = request.form.get('email','')
  # Check the validity of the username.
  if Util.checkUsername(username) and password == confirm_password:
    # If the username was valid, attempt to register the user.
    if dbm.register_user(username, password):
      # settings page.
      session['user'] = username
      return redirect('/user')
    # If the registration was not successful, keep them here and
    # tell them the error.
    return render_template('register.html', message='Username taken.')
  # If their username was invalid, tell them so.
  return render_template('register.html', message='Invalid username or password')


### USER SETTINGS PAGE
@app.route('/user')
def user():
    user = session.get('user', None)
    if not user:
        return render_template('register.html',
                               message='You are not a registered user!')
    userdata = dbm.get_user_by_username(user)
    return render_template('user.html', userdata=userdata)

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0", port=8000)
