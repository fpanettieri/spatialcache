from constants.parameters import ZOOM, BBOX
from bbox import BBox

from tiles import TilesManager
from logger import Logger
from params import ParamsDict

class Seeder():
   	
	def seed(self, params):
		
		# How many levels should we work with
		if params.has_key(ZOOM):
			zoom = int(params[ZOOM])
			Logger().info("Seeding %d zoom levels" % zoom)
			params.pop(ZOOM, None)
		else:
			Logger().warning("Zoom level not defined")
			zoom = 1
		
		# Parse bbox
		bbox = BBox()
		bbox.parse(params[BBOX])
		
		# Dictionary used to make requests
		aux_dict = ParamsDict(params.copy())
		
		# Generate tiles
		tilesManager = TilesManager()
		for i in xrange(zoom):
			for current_bbox in bbox.zoom(i):
				aux_dict[BBOX] = current_bbox
				tilesManager.getTile(aux_dict)
