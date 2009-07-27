import re
from constants.parameters import ZOOM
from bbox import BBox

from tiles import TilesManager


class Seeder:
	def seed(self, request, parameters):
		
		# How many levels should be generated
		if parameters.has_key(ZOOM):
			zoom = int(parameters[ZOOM])
		else:
			zoom = 1
		
		# Remove BBOX param from original request
		bbox_str = re.search("BBOX=.*?(&|$)", request, re.IGNORECASE).group()
		request = re.sub(bbox_str, "", request)
		
		# Parse bbox
		bbox = BBox()
		bbox.parse(bbox_str)
		
		# Generate tiles
		tilesManager = TilesManager()
		for i in xrange(zoom):
			for current_bbox in bbox.zoom(i):
				 full_request = request + current_bbox
				 tilesManager.getTile(full_request)
	
	
	def getBBOX(self, request):
		bbox_str = re.search("BBOX=.*?(&|$)", request, re.IGNORECASE).group()[5:]
		return urllib.unquote(bbox_str).split(',')

	
	def clean(self, request, parameters):
		pass
