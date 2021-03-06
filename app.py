from flask import Flask
from flask import redirect, render_template, request, session
import datetime
time = datetime.datetime.now()

import utils
##from server.database_manager import DatabaseManager

app = Flask(__name__)
'''
dbm = DatabaseManager.create()
'''
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    year = str(time.year)
    month = str(time.month)
    if len(month) == 1:
        month = '0' + month
    day = time.day
    nba_schedule = utils.NBA_D_Sched(year, month, day) ## daily schedule

    if request.method == "GET":
        news = utils.getMostPop('mostviewed', 'sports', '7')
        weather = utils.getWeatherByCity('NY', 'New_York')
        return render_template('home.html', 
                               weather=weather, 
                               nba_schedule=nba_schedule, 
                               news=news)

    ## WEATHER ##
    weather = ''
    weather_input = request.form.get('location', '')
    weather_error_message = ''

    if weather_input.isdigit():
        try:
            weather = utils.getWeatherByZip(str(weather_input))
        except: 
            weather_error_message = "Bad Zipcode. Retry."
    else:
        weather_input = ' '.join(word[0].upper() + word[1:] for word in weather_input.split())
        try: 
            weather_input_city = weather_input[0:weather_input.index(',')]
            weather_input_city = weather_input_city.replace (" ", "_").strip()
            weather_input_state = weather_input[weather_input.index(',')+1:].upper().strip()
            weather = utils.getWeatherByCity(str(weather_input_state), str(weather_input_city))
        except: 
            weather_error_message = "Cannot find city. Try again."
    ## NYT Section ##
    section = request.form.get('section', '')
    print section
    
    if section == '':
        section = 'sports' #default
    news = utils.getMostPop('mostviewed', section, '7')
    return render_template('home.html', 
                           weather = weather, 
                           weather_error_message=weather_error_message,
                           nba_schedule=nba_schedule, 
                           news=news)
    




@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/nba_standings')
def schedule():
    standings = utils.getStandings('2015')
    return render_template('nba_standings.html',standings=standings )

if __name__ == '__main__':
  app.debug = True
  app.secret_key = 'blah'
  app.run(host="0.0.0.0", port=8000)


'''
COULD NOT FIGURE OUT THE PURPOSE OF LOGIN/LOGOUT
AND WERE SHORT ON TIME DUE TO PREVIOUS COMPLICATIONS



### LOGIN
## taken from David and Alvin's api-project, WeatherText
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = session.get('user', None)
    if user:
        return redirect('/user_settings')
    if request.method == 'GET':
        return render_template('login.html')
    
    # Logs the user in if they are authorized.
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if dbm.authenticate(username, password):
        session['user'] = username
        return redirect('/user_settings')
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
  ## Check the validity of the username.
  # print dbm.get_all_users()
  # print "check0"
  # print username
  # print Util.checkUsername(username)
  # print password
  # print confirm_password

  if Util.checkUsername(username) and password == confirm_password:
    #print "check1"
    # If the username was valid, attempt to register the user.
    if dbm.register_user(username, password):
      #print "check2"
      # settings page.
      session['user'] = username
      return redirect('/user_settings')
    # If the registration was not successful, keep them here and
    # tell them the error.
    return render_template('register.html', message='Username taken.')
  # If their username was invalid, tell them so.
  return render_template('register.html', message='Invalid username or password')


### USER SETTINGS PAGE
@app.route('/user_settings')
def user_settings():
    user = session.get('user', None)
    if not user:
        return render_template('register.html',
                               message='You are not a registered user!')
    userdata = dbm.get_user_by_username(user)
    return render_template('user.html', username=user, userdata=userdata)
'''

