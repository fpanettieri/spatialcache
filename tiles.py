import os
import urllib

from hashlib import md5

from patterns import Singleton
from logger import Logger

from constants.http.status import OK, NOT_FOUND
from constants.error import REQUEST_FAILED

class TilesManager(Singleton):
	
	def configure(self, cfg):
		Logger().info("Configuring Tiles Manager")
		self.filters = []
		self.tilesPath = cfg.tilesPath
		self.wms = cfg.wms
		
		Logger().info("Parsing filters")
		for filter in cfg.filters:
			self.filters.insert(filter.order - 1, filter)
		Logger().info("Filters parsed")
		
		Logger().info("Tiles Manager configured")
	
	def getTile(self, params):
		"""
		Returns the tile from the cache if it exists, if not 
		"""
		result = ""
		tile_dir = self.tileDir(params)
		tile_path = os.path.join(tile_dir, params.hash())
		
		response_code = NOT_FOUND
		
		try:
			tile_file = open(tile_path, "r")
			result = tile_file.read()
			response_code = OK
		except:
			try:
				
				# Redirect request to WMS
				wms_request = self.wms + str(params)
				
				opener = urllib.FancyURLopener()
				
				response = opener.open(wms_request)
				response_code = OK
				
				result = response.fp.read();
				
				response_header = result[2:5];
				
				if(response_header != "xml"):
					# Create the path
					dir = os.path.dirname(tile_path)
					if not os.path.exists(dir):
						os.makedirs(dir)
					
					# Store tile in cache
					tile_file = open(tile_path, "w")
					tile_file.write(result)
					tile_file.close()
				else:
					Logger().error(REQUEST_FAILED + wms_request + result)
					response_code = NOT_FOUND
					result = ""
			except:
				response_code = NOT_FOUND
				Logger().warning(REQUEST_FAILED + wms_request)
		finally:
			return result, response_code
	
	def tileDir(self, params):
		"""
		Use the current configuration to convert the given parameters into a valid path
		where the tile that should be stored
		"""
		path = self.tilesPath
		for filter in self.filters:
			dir = ""
			if params.has_key(filter.name):
				dir = filter.name + "=" + params[filter.name]
			if filter.hash and dir != "":
				dir = md5(dir).hexdigest()
			path = os.path.join(path, dir)
		return path