#!/usr/bin/env python
import struct
import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt


class dynaplot:
    def __init__(self, max_x = 4096, window_size = 512):
        self.y_values = []
        self.x_values = []
        self.max_x = max_x
        self.window_size = window_size
        self.counter = 0
        self.fig, self.ax = plt.subplots(1, 1)
        self.ax.set_xlim(0, max_x)
        # self.ax.hold(True)
        plt.show(False)
        plt.draw()
        self.points = plt.plot(self.x_values,self.y_values)[0]
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)

    """
    Display using matplotlib
    """
    def plot(self, x_value, y_value):
        self.x_values.append(x_value)
        self.y_values.append(y_value)
        # self.ax.set_xlim(min(self.x_values), max(self.x_values))
        # self.ax.set_ylim(min(self.y_values), max(self.y_values))
        if (len(self.x_values) > self.max_x):
            self.x_values.pop(0)
            self.y_values.pop(0)
        self.counter = (self.counter + 1) % self.window_size
        if (self.counter == 0):
            self.points.set_data(np.fft.fft(self.y_values))
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
