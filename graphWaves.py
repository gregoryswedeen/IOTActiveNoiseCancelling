from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi
import numpy as np

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 5.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

time = arange(0.0, duration, (f/fs))
fig = figure(1)

#Wave 1
wave1 = sin(2*pi*time).astype(np.float32)
#Graphing
graph1 = fig.add_subplot(211)
graph1.plot(time, sin(2*pi*time))
graph1.grid(True)
graph1.set_ylim((-2, 2))
graph1.set_ylabel('1 Hz')
graph1.set_title('A sine wave or two')

for label in graph1.get_xticklabels():
    label.set_color('r')

#Wave2
wave2 = sin(2*pi*time + pi).astype(np.float32)
#Graphing
graph2 = fig.add_subplot(212)
graph2.plot(time, sin(2*pi*time + pi)) #the plus pi adds a 90 phase shift
graph2.grid(True)
graph2.set_ylim((-2, 2))
title = graph2.set_xlabel('Interference Waves')
title.set_color('g')
title.set_fontsize('large')

show()
