from constants.general import PID_FILE

import os
import platform

from logger import Logger

def writePID():
	system_name = platform.system().lower()

	if "linux" in system_name:
		try:
			pid_file = open(PID_FILE, "w")
			pid_file.write(str(os.getpid()))
			pid_file.close()
		except:
			Logger().warning("PID couldn't be written")
