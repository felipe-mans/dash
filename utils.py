import urllib2, json

#api key: bac9dac8506a2912
def getWeather(CityName):
  f = urllib2.urlopen('http://api.wunderground.com/api/Your_Key/geolookup/conditions/q/IA/Cedar_Rapids.json')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  location = parsed_json['location']['city']
  temp_f = parsed_json['current_observation']['temp_f']
  print "Current temperature in %s is: %s" % (location, temp_f)
  f.close()
