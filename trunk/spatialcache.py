#!/usr/bin/env python

from logger import Logger
from config import Configuration
from server import CacheServer
from daemon import Daemon
from tiles import TilesManager

class SpatialCache(Daemon):
	"""
	Application main class
	It has the responsibility to instantiate, initialize, and configure all
	the application services/modules
	"""
	def __init__(self):
		self.logger = Logger()
		self.config = Configuration()
		self.server = CacheServer()
		self.tilesManager = TilesManager()
	
	def configure(self, cfgfile):
		self.config.load(cfgfile)
		self.logger.configure(self.config.logger)
		self.tilesManager.configure(self.config.tiles)
		self.server.configure(self.config.server)
		if self.config.general.daemon:
			self.logger.info("Running as daemon")
			self.daemonize()
	
	def start(self):
		self.server.start()
	
	def stop(self):
		self.server.stop()
		
if __name__ == '__main__':
	
	from constants.general import CONFIGURATION_FILE, HELP_FILE, VERSION
	import sys
	
	# Import Psyco if available
	try:
		import psyco
		psyco.full()
	except ImportError:
		pass

	# TODO: Extract argument parsing method
	cfgfile = CONFIGURATION_FILE
	
	# Parse params
	for i in range(len(sys.argv)):
		if sys.argv[i] == "-c":
			cfgfile = sys.argv[i+1]
		elif sys.argv[i] == "-h":
			print open(HELP_FILE).read()
			sys.exit()
		elif sys.argv[i] == "-v":
			print VERSION
			sys.exit()
	
	cache = SpatialCache()
	cache.configure(cfgfile)
	cache.start()
