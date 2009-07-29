from SocketServer import ThreadingTCPServer
from handler import CacheRequestHandler
from logger import Logger

class CacheServer():
	"""
	This class has the responsibility to listen and answer requests done by
	different clients
	"""	
	def __init__(self):
		self.logger = Logger()
	
	def configure(self, cfg):
		self.logger.info("Configuring Server")
		self.host = cfg.host
		self.port = cfg.port
		self.logger.info("Server configured")
		
	def start(self):
		"""Start cache and administration services"""
		server_address = (self.host, self.port)
		self.logger.info("Starting server on %s:%s" % server_address)
		self.server_instance = ThreadingTCPServer(server_address, CacheRequestHandler)
		self.server_instance.serve_forever()
	
	def stop(self):
		"""Stop running services"""
		if self.server_instance:
			self.server_instance.server_close()
			self.logger.info("Stopping server")
