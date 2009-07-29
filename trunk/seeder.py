import re
from constants.parameters import ZOOM, BBOX
from bbox import BBox

from tiles import TilesManager
from threading import Thread


class Seeder(Thread):
	
	def __init__ (self, parameters):
		Thread.__init__(self)
		self.parameters = parameters
    
	def run(self):
		# How many levels should we work with
		if parameters.has_key(ZOOM):
			zoom = int(parameters[ZOOM])
		else:
			zoom = 1
		
		pass
   	
	def seed(self, request, parameters, zoom):
		
		
			
		# Remove extra param
		parameters.pop(ZOOM, None)
		
		# Parse bbox
		bbox = BBox()
		bbox.parse(parameters[BBOX])
		
		# Generate tiles
		tilesManager = TilesManager()
		for i in xrange(zoom):
			for current_bbox in bbox.zoom(i):
				 full_request = request + current_bbox
				 tilesManager.getTile(full_request)
	
	def clean(self, request, parameters):
		pass
