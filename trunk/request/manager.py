from hashlib import md5
from patterns import Monostate
import os
import re
import util

from constants.parameters import QUERY_MARK

class RequestManager(Monostate):

	def configure(self, cfg):
		self.filters = []
		self.tilesPath = cfg.tilesPath
		self.wms = cfg.wms
		for filter in cfg.filters:
			self.filters.insert(filter.order - 1, filter)
	
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
	
	def wmsRequest(self, path):
		return self.wms + path

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