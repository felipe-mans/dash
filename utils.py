import urllib2, json

# api key: bac9dac8506a2912
# Needs State abbreviation
# Needs City name
def getWeather(StateAbbrv, CityName):
  f = urllib2.urlopen('http://api.wunderground.com/api/bac9dac8506a2912/geolookup/conditions/q/NY/Forest_Hills.json')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  location = parsed_json['location']['city']
  temp_f = parsed_json['current_observation']['temp_f']
  result = "Current temperature in %s is: %s" % (location, temp_f)
  f.close()
  return result
