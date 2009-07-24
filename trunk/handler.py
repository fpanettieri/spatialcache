from BaseHTTPServer import BaseHTTPRequestHandler

from logger import Logger
from tiles import TilesManager

from constants.parameters import FORMAT, CONTENT_TYPE
from constants.error import UNEXPECTED_ERROR

class CacheRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		try:
			# Parse the parameters
			tilesManager = TilesManager()
			parameters = tilesManager.parseParameters(self.path)
			tile = tilesManager.getTile(self.path, parameters)
			
			# Send headers
			self.send_response(200)
			if parameters.has_key(FORMAT):
				self.send_header(CONTENT_TYPE, parameters[FORMAT])
			self.end_headers()
			
			# Send tile
			self.wfile.write(tile)
		except:
			Logger().error(UNEXPECTED_ERROR)
