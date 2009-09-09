from constants.general import PID_FILE

import os
import platform

def writePID():
	system_name = platform.system().lower()

	if "linux" in system_name:
		pid_file = open(PID_FILE, "w")
		pid_file.write(str(os.getpid()))
		pid_file.close()

