import urllib2, json

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
  key = ''
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
    return result





#----------------------- Testing Statements --------------------------------

#print getWeatherByZip(10024)
#print getWeatherByZip(90210)
#print getWeatherByZip(94101)
#print getWeatherByCity('CA', 'San_Francisco')
#print getWeatherByCity('NY', 'Brooklyn')
#print getWeatherByCity('CA', 'Los_Angeles')
print getTopStories('home')
