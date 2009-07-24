#!/usr/bin/env python

import sys
import tempfile
sys.path.append("..")

from config import Config

# Create tmp file with sample data
file_handler, file_path = tempfile.mkstemp(".xml")

xmlcontent = """
<options>
  <host>someHost</host>
  <port>4765</port>
  <tilesPath>/tmp/tiles</tilesPath>
  <server>http://localhost:8080/wms</server>
</options>
"""

# Tested configuration
file = tempfile.NamedTemporaryFile(delete=False)
file.write(xmlcontent)
file.close()

cfg = Config()
cfg.load(file.name)
    
assert cfg.host == "someHost"
assert cfg.port == 4765
assert cfg.tilesPath == "/tmp/tiles"
assert cfg.server == "http://localhost:8080/wms"
