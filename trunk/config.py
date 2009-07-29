import xml.etree.ElementTree as ETree
from patterns import DynamicObject
from util import strToBool

class Configuration():
	"""
	This class manages all the configuration
	It has the responsibility to read and save configuration files
	"""
	def load(self, file):
		"""
		Parse file to retrieve properties
		"""
		xml = ETree.parse(file)
		
		self.general = DynamicObject()
		self.general.daemon = strToBool(xml.find("General/Daemon").text)

		self.server = DynamicObject()
		self.server.host = xml.find("Server/Host").text
		self.server.port = int(xml.find("Server/Port").text)
		
		self.logger = DynamicObject()
		self.logger.logLevel = xml.find("Logger/LogLevel").text
		self.logger.logFile = xml.find("Logger/LogFile").text
		self.logger.failsafeLogFile = xml.find("Logger/FailsafeLogFile").text
		self.logger.logMaxLenght = int(xml.find("Logger/LogMaxLenght").text)
		self.logger.smtpHost = xml.find("Logger/SMTPHost").text
		self.logger.emailSender = xml.find("Logger/EmailSender").text
		self.logger.emailReceivers = xml.find("Logger/EmailReceivers").text
		self.logger.fileLogLevel = xml.find("Logger/FileLogLevel").text
		self.logger.smtpLogLevel = xml.find("Logger/SMTPLogLevel").text

		self.tiles = DynamicObject()
		self.tiles.tilesPath = xml.find("Tiles/TilesPath").text
		self.tiles.wms = xml.find("Tiles/WMS").text
		self.tiles.filters = []
		for it in xml.findall("Tiles/Filters/Filter"):
			filter = DynamicObject()
			filter.name = it.find("Name").text
			filter.order = int(it.find("Order").text)
			filter.hash = strToBool(it.find("Hash").text)
			self.tiles.filters.append(filter)
	
	def write(self, file):
		"""
		Write properties to file
		"""
		pass
