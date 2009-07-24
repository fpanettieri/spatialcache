def strToBool(str):
	"""Converts a boolean string into a real boolean value"""
	return (str.lower().strip() == "true")

def systemlog(text):
	"""Logs into a special file whenever the logger it's not available"""
	file = open('system.log', 'a+')
	line = "Systemlog: " + text + "\n"
	file.write(line)
	file.close()
