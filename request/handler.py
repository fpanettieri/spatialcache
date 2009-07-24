import os, urllib
from BaseHTTPServer import BaseHTTPRequestHandler

from request.manager import RequestManager
from logger import Logger
import util

from constants.parameters import FORMAT, CONTENT_TYPE, ACTION
from constants.error import REQUEST_FAILED, UNEXPECTED_ERROR

class CacheRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		# Parse the parameters
		requestManager = RequestManager()
		parameters = requestManager.parseParameters(self.path)
		tile = requestManager.tilePath(self.path, parameters)
		
		# Send headers
		self.send_response(200)
		if parameters.has_key(FORMAT):
			self.send_header(CONTENT_TYPE, parameters[FORMAT])
		self.end_headers()
		
		# If the response exists, return it from the cache
		try:
			# Get response from the cache
			image = open(tile,"r")
			self.wfile.write(image.read())
		
		# Else, get it from the server
		except:
			try:
				# Redirect request to WMS
				wms_request = requestManager.wmsRequest(self.path)
				tile_bytes = urllib.urlopen(wms_request).read();
				self.wfile.write(tile_bytes)
				
				# Create the path
				dir = os.path.dirname(tile)
				if not os.path.exists(dir):
					os.makedirs(dir)
				
				# Store tile in cache
				# TODO: Handle and log name collision
				img_file = open(tile, "w")
				img_file.write(tile_bytes)
				img_file.close()
			except IOError:
				Logger().warning(REQUEST_FAILED + wms_request)
			except:
				Logger().error(UNEXPECTED_ERROR)
	
	def do_POST(self):
		self.send_response(301)
		self.end_headers()
		requestManager = RequestManager()
		parameters = requestManager.parseParameters(self.path, self.rfile.read())
		# TODO: Delegate action to the corresponding manager
		# action = parameters[ACTION]
	
# TODO server administration
