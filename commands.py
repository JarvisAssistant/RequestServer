import datetime

def get_time():
	dt = datetime.datetime.now()

	return {
		"year" : dt.year,
		"month" : dt.month,
		"day" : dt.day,
		"hour" : dt.hour,
		"minute" : dt.minute,
		"second" : dt.second
	}
