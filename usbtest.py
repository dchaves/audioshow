#!/usr/bin/env python
import time
from usbcolors import USBColors

if __name__ == '__main__':
	usbcolors = USBColors()
	usbcolors.set_color(usbcolors.BLACK)
	print("Black")
	time.sleep(1)
	i = 0
	while i < 500:
		i = (i + 1) % 512
		usbcolors.set_RGB(0,i,0)
		#time.sleep(0.001)
		#print("Green ",i)
	usbcolors.set_RGB(0,0,0)
	print("Black")
	time.sleep(1)
	usbcolors.stop()
