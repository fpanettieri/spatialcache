"""
Used to test POST and GET requests
"""
import urllib

def testPOST():
	urllib.urlopen("http://localhost:5001/wms?REQUEST=getMap&LAYERS=dv_:lots", urllib.urlencode({"ACTION": "seed", "ZOOM": "3"}))
	
def testGET():
	urllib.urlopen("http://localhost:5001/wms?REQUEST=getMap&LAYERS=dv_:lots")
	
	
testGET()
testPOST()
