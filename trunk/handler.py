from BaseHTTPServer import BaseHTTPRequestHandler

from logger import Logger
from tiles import TilesManager
from seeder import Seeder
from cleaner import Cleaner
from params import ParamsDict

from constants.http.status import OK
from constants.parameters import FORMAT, CONTENT_TYPE
from constants.actions import SEED, CLEAN, ACTION
from constants.error import UNEXPECTED_ERROR

class CacheRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		try:
			# Parse the parameter
			parameters = ParamsDict()
			parameters.parse(self.path)
			tile, response_code = TilesManager().getTile(parameters)
			
			# Send headers
			self.send_response(response_code)
			if parameters.has_key(FORMAT):
				self.send_header(CONTENT_TYPE, parameters[FORMAT])
			self.end_headers()
			
			if(response_code == OK):
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
			
			# Check if action is defined
			action = SEED
			if params.has_key(ACTION):
				Logger().info("POST Action: %s" % ACTION)
				action = params[ACTION]
				params.pop(ACTION, None)
			
			if action == SEED:
				self._seed(params)
			elif action == CLEAN:
				self._clean(params)
			
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
			
			self._clean(params)
			
			# Send response
			self.send_response(200)
			self.end_headers()
			
		except:
			Logger().error(UNEXPECTED_ERROR)
	
	def _seed(self, params):
		Logger().info("Seeding: " + str(params))
		
		seeder = Seeder()
		seeder.seed(params)
		
		Logger().info("Finished seeding: " + str(params))
	
	def _clean(self, params):
		Logger().info("Cleaning: " + str(params))
		
		cleaner = Cleaner()
		cleaner.clean(params)
		
		Logger().info("Finished cleaning: " + str(params))
