## Simple ##
SpatialCache is cache server written entirely in python.
It has been designed to be flexible and powerful.

## Flexible ##
Even it has been designed to work with a WMS as backend, it can be used beyond this scope without any trouble.
You can use it as a general purpose cache if you want.
Think of it as a small squid, that show it's true power when serving WMS requests.

## Powerful ##
The multithreaded architecture makes it safe and scalable.
GET request have been optimized to be incredibly fast.
POST requests allows you to seed different zoom levels of a given request adding only a single param (Ex.: ZOOM=1,3,5-8).
DELETE requests are used to clean folders using params filters hierarchy that you have defined.

### Before you start: ###
Some basic knowledge about WMS and HTTP is assumed.

### Getting started: ###
  1. Download the last stable version from the website. (http://code.google.com/p/spatialcache)
  1. Unpack the file named spatialcache-x.x.tar.gz
  1. Set the path to your WMS in configuration.xml
  1. Start the server "python spatialcache.py -c configuration.xml"

### Requirements: ###
Python >= 2.5

### Recomeded: ###
Installing Psyco will make the server run faster.
