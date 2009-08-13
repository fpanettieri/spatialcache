from BaseHTTPServer import BaseHTTPRequestHandler

from logger import Logger
from tiles import TilesManager
from seeder import Seeder
from cleaner import Cleaner
from params import ParamsDict

from constants.parameters import FORMAT, CONTENT_TYPE
from constants.error import UNEXPECTED_ERROR

class CacheRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		try:
			# Parse the parameter
			parameters = ParamsDict()
			parameters.parse(self.path)
			tile = TilesManager().getTile(parameters)
			
			# Send headers
			self.send_response(200)
			if parameters.has_key(FORMAT):
				self.send_header(CONTENT_TYPE, parameters[FORMAT])
			self.end_headers()
			
			# Send tile
			self.wfile.write(tile)
		except:
			Logger().error(UNEXPECTED_ERROR)
	
	def do_POST(self):
		try:
			# Get post data
			content_length = int(self.headers["content-length"])
			post = self.rfile.read(content_length)
			
			# Parse the parameter
			params = ParamsDict()
			params.parse(post)
			
			# Log
			Logger().info("Seeding: " + str(params))
			
			# Launch seeder
			seeder = Seeder()
			seeder.seed(params)
			
			# Send headers
			self.send_response(200)
			self.end_headers()
			
		except:
			Logger().error(UNEXPECTED_ERROR)
			
	def do_DELETE(self):
		try:
			# Get post data
			content_length = int(self.headers["content-length"])
			post = self.rfile.read(content_length)
			
			# Parse the parameter
			params = ParamsDict()
			params.parse(post)
			
			# Log
			Logger().info("Cleaning: " + str(params))
			
			# Launch seeder
			cleaner = Cleaner()
			cleaner.clean(params)
			
			# Send headers
			self.send_response(200)
			self.end_headers()
			
		except:
			Logger().error(UNEXPECTED_ERROR)
