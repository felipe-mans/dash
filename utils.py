import urllib2, json


#Parameters: Abbreviation of the state, the name of the city
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

#Parameters: Section of the New York Times (home, sports, etc.)
def getTopStories(section):
  key = ''
  f = urllib2.urlopen('http://api.nytimes.com/svc/topstories/v1/%s.json?api-key=%s' % (section, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  i = 0
  result = '\n'
  while (i < 5 ):
    result = result + parsed_json['results'][i]['title'] + '\n'
    i = i+1
  return result
    
#print getWeatherByCity('CA', 'San_Francisco') 
#print getWeatherByCity('NY', 'Brooklyn')
#print getWeatherByCity('CA', 'Los_Angeles')
print getTopStories('home')

#Parameters: Zipcode of the area you want (in the U.S.)
def getWeatherByZip(zip):
  key = ""

  f = urllib2.urlopen('http://api.wunderground.com/api/%s/geolookup/conditions/q/%s.json' % (key, zip))
  #http://api.wunderground.com/api/Your_Key/forecast/q/CA/San_Francisco.json
  json_string = f.read()
  parsed_json = json.loads(json_string)
	
  location = parsed_json['location']['city']
  temp_f = parsed_json['current_observation']['temp_f']
  weather = parsed_json['current_observation']['weather']
  
  result = ('%s (%s): %s. %s degrees F.' % (location, zip, weather, temp_f))
  f.close()
  return result

#print getWeatherByZip(10024)
#print getWeatherByZip(90210)
#print getWeatherByZip(94101)
