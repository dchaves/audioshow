#!/usr/bin/env python
import threading
from pyftdi.gpio import GpioController, GpioException
import numpy as np

class USBColors(threading.Thread):
	"""
	"""
	BLUE = 0x01
	GREEN = 0x02
	RED = 0x08
	WHITE = RED | GREEN | BLUE
	BLACK = 0x00
	LOOP_MAX = 512


	def __init__(self, ftdi_url = 'ftdi://ftdi:232r/1'):
		threading.Thread.__init__(self)
		self.gpio = GpioController()
		self.state = 0
		self.ftdi_url = ftdi_url
		self.exitFlag = False
		self.sequence = [self.BLACK] * self.LOOP_MAX
		self.ledstatus = self.WHITE
		self.lock = threading.Lock()
		self.open()
		self.start()

	def run(self):
		while not self.exitFlag:
			with self.lock:
				syncseq = self.sequence
			for i in range(0, self.LOOP_MAX):
				self.ledstatus = (self.ledstatus & (~syncseq[i] & self.WHITE))
				self.ledstatus = (self.ledstatus | (~syncseq[i] & self.WHITE))
				self.gpio.write_port(self.ledstatus)
				if self.exitFlag:
					break

	def stop(self):
		self.exitFlag = True
		self.gpio.write_port(self.WHITE)
		self.join()
		self.gpio.close()

	def open(self):
		self.gpio.open_from_url(self.ftdi_url, self.WHITE)

	def set_color(self, color):
		self.sequence = [color] * self.LOOP_MAX

	def set_RGB(self, red_intensity, green_intensity, blue_intensity):
		red_indexes = list(set(np.floor(np.linspace(0, self.LOOP_MAX, red_intensity))))
		green_indexes = list(set(np.floor(np.linspace(0, self.LOOP_MAX, green_intensity))))
		blue_indexes = list(set(np.floor(np.linspace(0, self.LOOP_MAX, blue_intensity))))

		#print("RED - ", red_indexes)
		#print("GREEN - ", green_indexes)
		#print("BLUE - ", blue_indexes)
		seq = [0] * self.LOOP_MAX
		for i in range(0,self.LOOP_MAX):
			if i in red_indexes:
				seq[i] += self.RED
			if i in green_indexes:
				seq[i] += self.GREEN
			if i in blue_indexes:
				seq[i] += self.BLUE
		with self.lock:
			self.sequence = seq
			# self.sequence = [self.BLACK] * self.LOOP_MAX
			#print("SEQ - ", self.sequence)
