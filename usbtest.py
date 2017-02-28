#!/usr/bin/env python
from usbcolors import USBColors

if __name__ == '__main__':
	usbcolors = USBColors()
	usbcolors.open()
	usbcolors.set_color(usbcolors.BLACK)
	usbcolors.set_intensity(usbcolors.RED, )
	usbcolors.close()
