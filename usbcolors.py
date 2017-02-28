#!/usr/bin/env python

from pyftdi.gpio import GpioController, GpioException

class USBColors(object):
	"""
	"""
	BLUE = 0x01
	GREEN = 0x02
	RED = 0x08
	WHITE = RED | GREEN | BLUE
	BLACK = 0x00

	def __init__(self, ftdi_url = 'ftdi://ftdi:232r/1'):
		self.gpio = GpioController()
		self.state = 0
		self.ftdi_url = ftdi_url

	def open(self):
		self.gpio.open_from_url(self.ftdi_url, self.WHITE)

	def close(self):
		self.gpio.close()

	def set_color(self, color):
		self.gpio.write_port(self.WHITE & ~color)

	def set_intensity(self, color, intensity):
		index = 0
		while True:
			if(index < intensity):
				self.set_color(color)
			else:
				self.set_color(self.BLACK)
			index = (index + 1) % (intensity + 1)
