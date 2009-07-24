from SocketServer import ThreadingTCPServer
from handler import CacheRequestHandler

class CacheServer():
	"""
	This class has the responsibility to listen and answer requests done by
	different clients
	"""	
	def configure(self, cfg):
		self.host = cfg.host
		self.port = cfg.port
		
	def start(self):
		"""Start cache and administration services"""
		server_address = (self.host, self.port)
		self.server_instance = ThreadingTCPServer(server_address, CacheRequestHandler)
		self.server_instance.serve_forever()
	
	def stop(self):
		"""Stop running services"""
		if self.server_instance:
			self.server_instance.server_close()
