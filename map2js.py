#!/usr/bin/env python

__author__ = "mathieu@garambrogne.net"
__version__ = "0.0.1"

import Image
import sys

class Zone(object):
	def __init__(self, top, left):
		self.top = top
		self.bottom = top
		self.right= left
		self.left = left
	def bottomRight(self, bottom, right):
		self.bottom = bottom
		self.right = right
	def __repr__(self):
		return "<Zone %i,%i,%i,%i>" % (self.top, self.right, self.bottom, self.left)
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
						self.zones[(r,g,b)] = Zone(x, y)
					self.zones[(r,g,b)].bottomRight(x,y)

if __name__ == '__main__':
	m = ImageMap(Image.open('map.png'))
	m.scan()
	print m.zones
