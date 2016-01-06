import urllib2, json

# Needs State abbreviation
# Needs City name
def getWeatherByCity(StateAbbrv, CityName):
  f = urllib2.urlopen('http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json' % (Key, StateAbbrv, CityName))
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
  f = urllib2.urlopen('http://api.nytimes.com/svc/topstories/v1/%s.JSON?api-key=%s' % (section, key))
  json_string = f.read()
  parsed_json = json.loads(json_string)
  print parsed_json


print getWeatherByCity('CA', 'San_Francisco') 
print getWeatherByCity('NY', 'Brooklyn')
print getWeatherByCity('CA', 'Los_Angeles')
print getTopStories('sports')
