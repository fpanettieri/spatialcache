import sys

def strToBool(str):
	"""Converts a boolean string into a real boolean value"""
	return (str.lower().strip() == "true")

def systemlog(text):
	"""Logs into a special file whenever the logger it's not available"""
	file = open('system.log', 'a+')
	line = "Systemlog: " + text + "\n"
	file.write(line)
	file.close()

def workingPath():
	"""Return the current working path"""
	return sys.path[0]

def truncate(f, n=2):
	"""
	Truncate an float to the given length (slow) 
	"""
	float_str = ('%.*f' % (n + 1, f)).rstrip('0')
	sp = float_str.split('.')
	ret_val = sp[0]
	if len(sp) > 1 and sp[1]:
		ret_val += '.' + sp[1][:n]
	return ret_val

def readFile(filename):
        try:
                file = open(filename)
                bytes = file.read()
        except:
                bytes = []
        finally:
                file.close()
        return bytes

