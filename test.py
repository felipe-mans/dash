import datetime

foo = datetime.datetime.now()
print "it's " + '/'.join(str(n) for n in [foo.month, foo.day, foo.year]) + " and the time is " + ':'.join(str(n) for n in [foo.hour % 12, foo.minute, foo.second])
