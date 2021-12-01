from time import time, sleep
from math import pi, sin
from time import time, sleep, time_ns
import numpy as np
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['font.family'] = 'Times New Roman'

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlabel='time [s]', ylabel='pressure [Pa]')

P0 = []
P1 = []
P2 = []
P3 = []
P4 = []
P5 = []
P6 = []

T0 = []
T1 = []
T2 = []
T3 = []
T4 = []
T5 = []
T6 = []


colors = ['green', 'blue', 'red', 'yellow',
          'black', 'orange', 'magenta', 'cyan']
line0, = ax.plot(T0, P0, color=colors[0], label=colors[0])
line1, = ax.plot(T1, P1, color=colors[1], label=colors[1])
line2, = ax.plot(T2, P2, color=colors[2], label=colors[2])
line3, = ax.plot(T3, P3, color=colors[3], label=colors[3])
line4, = ax.plot(T4, P4, color=colors[4], label=colors[4])
line5, = ax.plot(T5, P5, color=colors[5], label=colors[5])
line6, = ax.plot(T6, P6, color=colors[6], label=colors[6])

lines = [line0, line1, line2, line3, line4, line5, line6]
Ps = [P0, P1, P2, P3, P4, P5, P6]
Ts = [T0, T1, T2, T3, T4, T5, T6]

start = time_ns()
count = 0
period = 0.01
while count < 5000:
    count += 1
    sleep(period)
    print(count)
    try:
        # data = sensors[i]()
        current_time = (time_ns()-start)*10**-9
        data = {"depth": sin(current_time)}
        print(data)
        for i in range(7):
            Ps[i].append(data["depth"]*i)
            Ts[i].append(current_time)
            lines[i].set_ydata(Ps[i])
            lines[i].set_xdata(Ts[i])

        ax.relim()
        ax.autoscale()
        fig.canvas.draw()
        plt.pause(0.0001)
        plt.legend()
    except KeyboardInterrupt:
        plt.close('all')
        break