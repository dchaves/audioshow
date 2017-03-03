#!/usr/bin/env python
import time
from usbcolors import USBColors

if __name__ == '__main__':
	usbcolors = USBColors()
	usbcolors.set_color(usbcolors.BLACK)
	time.sleep(10)
	usbcolors.set_RGB(512,255,0)
	time.sleep(10)
	usbcolors.set_RGB(0,0,0)
	usbcolors.stop()
