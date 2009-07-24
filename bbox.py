import urllib

class BBox:
	def __init__(self, bbox_str):
		limits = urllib.unquote(bbox_str).split(",")
		self.minX = limits[0]
		self.minY = limits[1]
		self.maxX = limits[2]
		self.maxY = limits[3]
	
	def zoom(self, zoom_level):
		return []
		
