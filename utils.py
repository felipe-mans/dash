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

top10 = getTopStories('home')
for i in top10:
  print i
  print "\n"

print "\n\n\n NEXT \n\n\n"

mostpop = getMostPop('mostviewed', 'sports', '1')
for i in mostpop:
  print i
  print "\n"
