import urllib
from util import truncate

class BBox:
	def __init__(self):
		self.minX = -180
		self.minY = -90
		self.maxX = 180
		self.maxY = 90
	
	def parse (self, bbox_str):
		limits = urllib.unquote(bbox_str).split(",")
		self.minX = float(limits[0])
		self.minY = float(limits[1])
		self.maxX = float(limits[2])
		self.maxY = float(limits[3])
	
	def zoom(self, zoom_level):
		tiles_total = 2**zoom_level
		tile_width = (self.maxX - self.minX) / tiles_total 
		tile_height = (self.maxY - self.minY) / tiles_total
		tiles = []
		
		for i in xrange(tiles_total):
			for j in xrange(tiles_total):
				minX = self.minX + i * tile_width 
				minY = self.minY + j * tile_height
				maxX = minX + tile_width
				maxY = minY + tile_height
				current_bbox = "%s,%s,%s,%s" % (_fmt(minX), _fmt(minY), _fmt(maxX), _fmt(maxY))
				tiles.append(urllib.quote(current_bbox))
		return tiles
	
def _fmt(f):
	#TODO: make this number configurable
	return truncate(f, 6)
