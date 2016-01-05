import urllib2, json

# api key: bac9dac8506a2912
# Needs State abbreviation
# Needs City name
def getWeatherByCity(StateAbbrv, CityName):
  f = urllib2.urlopen('http://api.wunderground.com/api/bac9dac8506a2912/geolookup/conditions/q/%s/%s.json' % (StateAbbrv, CityName))
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
  
print getWeatherByCity('CA', 'San_Francisco') 
print getWeatherByCity('NY', 'Brooklyn')
print getWeatherByCity('CA', 'Los_Angeles')

