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

#NYTIMES API
#Key: c64d2df8a7a0fcef44688bd7e18df8c9:14:73937184 (article search)
#Key: c47995663adcb790f7a5e8f921b24680:9:73937184 (most popular)
#Key: ae6374a908a1d1e71c4e91ae7d2fffb7:2:73937184 (top stories)







  
print getWeatherByCity('CA', 'San_Francisco') 
print getWeatherByCity('NY', 'Brooklyn')
print getWeatherByCity('CA', 'Los_Angeles')

