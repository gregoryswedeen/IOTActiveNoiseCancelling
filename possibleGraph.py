import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import numpy as np
import wave
import sys

wave1 = wave.open('wave1.wav','r')
wave2 = wave.open('wave2.wav','r')

fig = figure(1)

#Wave 3
wave1Signal = wave1.readframes(440)
wave1Signal = np.fromstring(wave1Signal, 'Int16')
fs1 = 44100
#Wave 2
wave2Signal = wave2.readframes(440)
wave2Signal = np.fromstring(wave2Signal, 'Int16')
fs2 = 44100


time1 =np.linspace(0, len(wave1Signal)/fs1, num=len(wave1Signal))
time2 =np.linspace(0, len(wave2Signal)/fs2, num=len(wave2Signal))

graph1 = fig.add_subplot(211)
graph1.plot(time1, wave1Signal)
graph1.grid(True)
graph1.set_ylim((-10000, 10000))
graph1.set_ylabel('1 Hz')
graph1.set_title('A sine wave or two')

graph2 = fig.add_subplot(212)
graph2.plot(time2, wave2Signal)
graph2.grid(True)
graph2.set_ylim((-10000, 10000 ))
title = graph2.set_xlabel('Interference Waves')
title.set_color('g')
title.set_fontsize('large')

show()