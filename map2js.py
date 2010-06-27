#!/usr/bin/env python
"""
Build a js map from an image
"""
__author__ = "mathieu@garambrogne.net"
__version__ = "0.0.1"

import Image

class Zone(object):
	def __init__(self, color, top, left):
		self.color = color
		self.top = top
		self.bottom = top
		self.right= left
		self.left = left
	def bottomRight(self, bottom, right):
		self.bottom = bottom
		self.right = right
	def __repr__(self):
		return "<Zone %i,%i,%i,%i>" % (self.top, self.right, self.bottom, self.left)
	def rect(self):
		return (self.top, self.right, self.bottom, self.left)
	def toJson(self):
		return """{color:"%s", top:%i, right:%i, bottom:%i, left:%i}""" % (hexcolor(self.color), self.top, self.right, self.bottom, self.left)
class ImageMap(object):
	def __init__(self, image):
		self.image = image
		self.zones = {}
	def scan(self):
		w,h = self.image.size
		for x in range(w):
			for y in range(h):
				r,g,b,a = self.image.getpixel((x,y))
				if a > 0:
					#print r,g,b
					if (r,g,b) not in self.zones:
						self.zones[(r,g,b)] = Zone((r,g,b),x, y)
					self.zones[(r,g,b)].bottomRight(x,y)
	def dummyMap(self):
		f = open('map.js','w')
		f.write( "function zone(x, y) {\n")
		for color, zone in self.zones.items():
			t, r, b, l = zone.rect()
			f.write("""\tif(x >= %i && x <= %i && y >= %i && y <= %i) return %s;\n""" % (l,r,t,b,zone.toJson()))
		f.write("}\n")
def hexcolor(color):
	tmp = ''
	for c in color:
		tmp += ("0%x" % c)[-2:]
	return tmp

if __name__ == '__main__':
	m = ImageMap(Image.open('map.png'))
	m.scan()
	m.dummyMap()
	#print m.zones
