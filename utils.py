import urllib2, json, requests
from operator import itemgetter


#----------------------- API Functions ----------------------------------

#---------- getWeatherByCity ----------
#
# Will return the current weather of the given city
#
# Parameters: Abbreviation of the state, the name of the city
def getWeatherByCity(StateAbbrv, CityName):
  key = ""

  f = urllib2.urlopen('http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json' % (key, StateAbbrv, CityName))
  #http://api.wunderground.com/api/Your_Key/forecast/q/CA/San_Francisco.json
  json_string = f.read()
  parsed_json = json.loads(json_string)
  #print parsed_json
  location = parsed_json['location']['city']
  temp_f = parsed_json['current_observation']['temp_f']
  weather = parsed_json['current_observation']['weather']
  result = "%s: %s, %s degrees F." % (location, weather, temp_f)
  f.close()
  return result

#---------- getWeatherByZip ---------
#
# Will return the weather of the Zipcode  given
#
# Parameters: Zipcode of the area you want (in the U.S.)
def getWeatherByZip(zip):
  key = ""
  f = urllib2.urlopen('http://api.wunderground.com/api/%s/geolookup/conditions/q/%s.json' % (key, zip))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  location = parsed_json['location']['city']
  temp_f = parsed_json['current_observation']['temp_f']
  weather = parsed_json['current_observation']['weather']
  result = ('%s (%s): %s. %s degrees F.' % (location, zip, weather, temp_f))
  f.close()
  return result
                      


#---------- getTopStories ----------
#
# Will return the top 5 stories of the given section from the New York Time
#
# Parameters: Section of the New York Times (home, sports, etc.)
def getTopStories(section):
  key = 'ae6374a908a1d1e71c4e91ae7d2fffb7:2:73937184'
  f = urllib2.urlopen('http://api.nytimes.com/svc/topstories/v1/%s.json?api-key=%s' % (section, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)

  top10 = []
  i = 0
  while i < 10:
    data = parsed_json['results'][i]
    result = data['title'] + "\n" + data['byline'] + " | " + data['section'] + \
           "\n" + data['abstract'] + "\n" + data['url'] + "\n" + \
           data['published_date'] 
    top10.append(result)
    i += 1
  return top10

#---------- getMostPop ----------
#
# Will return the 10 most popular stories of the given section from the New York Times. Popularity can be determined by the most-viewed, most-emailed or most-shared articles.
# Can return the most popular stories in the last day, 7 days or 10 days
#
# Parameters: Specific option (mostviewed, mostemailed, or mostshared), Section of the New York Times (home, sports, etc.), Number of days that content appeared (1, 7 or 10)
def getMostPop(option, section, days):
  key = 'c47995663adcb790f7a5e8f921b24680:9:73937184'
  f = urllib2.urlopen('http://api.nytimes.com/svc/mostpopular/v2/%s/%s/%s.json?api-key=%s' % (option, section, days, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)

  mostpop = []
  i = 0
  result = ''
  while i < 5:
    data = parsed_json['results'][i]
    result = data['title'] + '\n' + data['byline'] + ' | ' + data['section'] + '\n' + data['abstract'] + '\n' + data['url'] + '\n' + data['published_date']
    i = i + 1
    mostpop.append(result)
  return mostpop



#----------------------- Testing Statements --------------------------------

#print getWeatherByZip(10024)
#print getWeatherByZip(90210)
#print getWeatherByZip(94101)
#print getWeatherByCity('CA', 'San_Francisco')
#print getWeatherByCity('NY', 'Brooklyn')
#print getWeatherByCity('CA', 'Los_Angeles')
'''
top10 = getTopStories('home')
for i in top10:
  print i
  print "\n"

print "\n\n\n NEXT \n\n\n"

mostpop = getMostPop('mostviewed', 'sports', '1')
for i in mostpop:
  print i
  print "\n"
'''

def NBA_D_Sched(year, month, day):
  key = 'vxanp3p3cspvv57g9sg7y3mh'
  f = urllib2.urlopen('http://api.sportradar.us/nba-t3/games/%s/%s/%s/schedule.json?api_key=%s' % ( str(year), str(month), str(day), key))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  games_json = parsed_json["games"]

  games = []

  for i in games_json:
    game = {}
    game['home_team'] = i["home"]["alias"]
    game['away_team'] = i["away"]["alias"]
    game['arena'] = i["venue"]["name"]
    game['city'] = i["venue"]["city"]
    standard_game_time_hr = 7
    standard_game_time_min = 0
    game_time_hr = int(i["scheduled"][11:13]) + standard_game_time_hr
    game_time_min = int(i["scheduled"][14:16]) + standard_game_time_min
    if game_time_min == 0:
	game_time_min = "00"
    game['time'] = str(game_time_hr) + ":" + str(game_time_min)
    game['TV_station'] = i["broadcast"]["network"]
    games.append(game)

  return games


# input: YYYY/MM/DD
# ex: 2016/01/13
NBAgames =  NBA_D_Sched(2016, 01  , 22 )

print NBAgames

for i in NBAgames:
  result = i['away_team'] + " @ " + i['home_team'] + "\n"
  result += i['time'] + "\n"
  result += i['arena'] + ", " + i['city'] + '\n'
  result += i['TV_station'] + '\n\n'
  print result


def NBA_League_Leaders(stat):
  key = 'vxanp3p3cspvv57g9sg7y3mh'
 # f = urllib2.urlopen('http://api.sportradar.us/nba-t3/seasontd/2015/REG/leaders.json?api_key=%s' % (key))
  f = requests.get('http://api.sportradar.us/nba-t3/seasontd/2015/REG/leaders.json?api_key=%s' % (key))
  print f
  '''
  json_string = f.json()
  parsed_json = json.loads(json_string)
  cats = parsed_json["categories"]
  #for i in cats:
  #  print i["name"]
  leaders = []
  for i in cats:
    if i["name"] == stat: 
      for j in i["ranks"]:
        leaders.append( {
                         "name": j["player"]["full_name"],
                         stat: j["average"][stat]
                         })
      sorted_leaders = sorted(leaders, key=itemgetter(stat), reverse=True) 
      return sorted_leaders
  '''
pts_leaders =  NBA_League_Leaders('points')
ass_leaders =  NBA_League_Leaders('assists')
rbs_leaders =  NBA_League_Leaders('rebounds')
blks_leaders = NBA_League_Leaders('blocks')
stl_leaders = NBA_League_Leaders('steals')
min_leaders = NBA_League_Leaders('minutes')
field_goals_made_leaders = NBA_League_Leaders('field_goals_made')

print pts_leaders
print ass_leaders
#print rbs_leaders
#print blks_leaders
#print stl_leaders
#print min_leaders
#print field_goals_made_leaders

