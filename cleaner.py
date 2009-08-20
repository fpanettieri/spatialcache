import os
import shutil

from tiles import TilesManager

class Cleaner():
	
	def clean(self, params):
		
		# Get configured filters
		tilesManager = TilesManager()
		tiles_dir = tilesManager.tileDir(params)
		
		if os.path.exists(tiles_dir):
			shutil.rmtree(tiles_dir)
