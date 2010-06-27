#!/usr/bin/env python

__author__ = "mathieu@garambrogne.net"
__version__ = "0.0.1"

import Image
import sys

class Rectangle(object):
	def __init__(self, color):
		self.color = color
		
class ImageMap(object):
	def __init__(self, image):
		self.image = image
	def scan(self):
		w,h = self.image.size
		for x in w:
			for y in h:
				pixel = self.image.getpixel((x,y))
				print pixel

if __name__ == '__main__':
	
