import urllib2, json

# Needs State abbreviation
# Needs City name

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

def getTopStories(section):
<<<<<<< HEAD
  key = ''
  f = urllib2.urlopen('http://api.nytimes.com/svc/topstories/v1/%s.json?api-key=%s' % (section, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  i = 0
  while (i < 5 ):
    print parsed_json['results'][i]['title']
    i = i+1
    
#print getWeatherByCity('CA', 'San_Francisco') 
#print getWeatherByCity('NY', 'Brooklyn')
#print getWeatherByCity('CA', 'Los_Angeles')
getTopStories('home')
=======
  key = ""

  f = urllib2.urlopen('http://api.nytimes.com/svc/topstories/v1/%s.JSON?api-key=%s' % (section, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  print parsed_json


print getWeatherByCity('CA', 'San_Francisco') 
print getWeatherByCity('NY', 'Brooklyn')
print getWeatherByCity('CA', 'Los_Angeles')

print getTopStories('sports')

# Needs State abbreviation
# Needs City name
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

print getWeatherByZip(10024)
print getWeatherByZip(90210)
print getWeatherByZip(94101)
>>>>>>> 5c01c4d8c174994a724b91362c2244ca49b9bbad
