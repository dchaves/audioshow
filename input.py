#!/usr/bin/env python
import struct
import numpy as np
import time
import collections
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt


class dynaplot:
    def __init__(self, max_x = 512):
        self.y_values = collections.deque(max_x * [0], max_x)
        self.x_values = collections.deque(range(max_x), max_x)
        self.fig, self.ax = plt.subplots(1, 1)
        self.ax.set_xlim(0, max_x)
        self.ax.set_ylim(-32768,32767)
        # self.ax.hold(True)
        plt.show(False)
        plt.draw()
        self.points = plt.plot(list(self.x_values),list(self.y_values))[0]
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)

    """
    Display using matplotlib
    """
    def plot(self, x_value, y_value):
        self.x_values.append(x_value)
        self.y_values.append(y_value)
        self.points.set_data(list(self.x_values),list(self.y_values))
        self.fig.canvas.restore_region(self.background)
        self.ax.draw_artist(self.points)
        self.fig.canvas.blit(self.ax.bbox)
        plt.pause(0.00001)


if __name__ == '__main__':
    audiofile = open("/tmp/audioout")
    plotter = dynaplot()
    x = 0
    while True:
        value = struct.unpack("<h", audiofile.read(2))
        plotter.plot(x, value)
        x += 1
        #print value
