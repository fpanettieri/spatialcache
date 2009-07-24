import logging
from logging.handlers import RotatingFileHandler, SMTPHandler

from patterns import Singleton
from util import systemlog

from constants.general import APPLICATION_NAME

class Logger(Singleton):
	def configure(self, cfg):
		"""Configures the Logger module"""
		self.configured = False
		self.log = logging.getLogger(APPLICATION_NAME)
		try:
			try:
				fileHandler = RotatingFileHandler(cfg.logFile, 'a+', cfg.logMaxLenght)
			except:
				fileHandler = RotatingFileHandler(cfg.failsafeLogFile, 'a+', cfg.logMaxLenght)
			fileHandler.doRollover()
			formatter = logging.Formatter("%(levelname)s %(asctime)s: %(message)s")
			fileHandler.setFormatter(formatter)
			fileHandler.setLevel(logging.DEBUG)
			self.log.addHandler(fileHandler)
		except Exception:
			systemlog("File logger configuration failed")
		
		try:
			subject_str = APPLICATION_NAME + ' error log'
			smtpHandler = SMTPHandler(cfg.smtpHost, cfg.emailSender, cfg.emailReceivers, subject_str)
			smtpHandler.setLevel(logging.ERROR)
			smtpHandler.setFormatter(formatter)
			self.log.addHandler(smtpHandler)
		except Exception:
			systemlog("SMTP Logger configuration failed")	
		self.configured = True
	
	def debug(self, text):
		"""Log a debug message"""
		if self.configured:
			self.log.debug(text)
	
	def info(self, text):
		"""Log an info message"""
		if self.configured:
			self.log.info(text)
	
	def warning(self, text):
		"""Log a warning message"""
		if self.configured:
			self.log.warning(text)
	
	def error(self, text):
		"""Log an error message"""
		if self.configured:
			self.log.error(text)
	
	def critical(self, text):
		"""Log a critical message"""
		if self.configured:
			self.log.critical(text)
