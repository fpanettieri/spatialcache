import os
import urllib

from hashlib import md5

from patterns import Monostate
from logger import Logger

from constants.parameters import QUERY_MARK
from constants.error import REQUEST_FAILED

class TilesManager(Monostate):

	def configure(self, cfg):
		self.filters = []
		self.tilesPath = cfg.tilesPath
		self.wms = cfg.wms
		for filter in cfg.filters:
			self.filters.insert(filter.order - 1, filter)
	
	def getTile(self, request, parameters=None):
		"""
		Returns the tile from the cache if it exists, if not 
		"""
		tile_bytes = ""
		
		if not parameters:
			parameters = self.parseParameters(request)
		tile_path = self.tilePath(request, parameters)
		
		try:
			tile_file = open(tile_path, "r")
			tile_bytes = tile_file.read()
		except:
			try:
				# Redirect request to WMS
				wms_request = self.wmsRequest(request)
				tile_bytes = urllib.urlopen(wms_request).read();
				
				# Create the path
				dir = os.path.dirname(tile_path)
				if not os.path.exists(dir):
					os.makedirs(dir)
				
				# Store tile in cache
				# TODO: Handle and log name collision
				tile_file = open(tile_path, "w")
				tile_file.write(tile_bytes)
				tile_file.close()
			except IOError:
				Logger().warning(REQUEST_FAILED + wms_request)
		finally:
			return tile_bytes
			
		
	
	def tilePath(self, request, parameters):
		"""
		Use the current configuration to convert the given request into a valid path
		where the tile that should be stored
		"""
		path = self.tilesPath
		for filter in self.filters:
			dir = ""
			if parameters.has_key(filter.name):
				dir = parameters[filter.name]
			else:
				# TODO: Handle error if the filter doesn't exist in the parameters list
				pass
			if filter.hash:
				dir = md5(dir).hexdigest()
			path = os.path.join(path, dir)
		return os.path.join(path, md5(request).hexdigest()) 
	
	def wmsRequest(self, request):
		return self.wms + request

	def parseParameters(self, path, post=None):
		"""
		Creates a dictionary of parameters
		"""
		# Remove prefix
		params = path[path.find(QUERY_MARK) + 1:]
		
		# Concatenate request and post parameters to handle both in the same way
		if post:
			params += "&" + post
		
		# Dictionary where parameters will be stored
		dict = {}
		
		for kv in params.split("&"):
			k, v = kv.split("=")
			dict[k] = v
		
		return dict
