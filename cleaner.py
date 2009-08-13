import os
import shutil
import hashlib

from constants.parameters import ZOOM, BBOX, ACTION
from bbox import BBox

from tiles import TilesManager
from logger import Logger
from params import ParamsDict

class Cleaner():
	
	def clean(self, params):
		
		# Get configured filters
		tilesManager = TilesManager()
		tiles_dir = tilesManager.tileDir(params)
		
		if os.path.exists(tiles_dir):
			shutil.rmtree(tiles_dir)