import numpy as np
import sounddevice as sd
from numpy import arange, sin, pi
from scipy.io import wavfile
import scipy.io

sd.default.samplerate = 44100

time = 30.0
frequency = 440

# Generate time of samples 
samples = np.arange(44100 * time) / 44100.0
# Sine formulas
wave = 10000 * np.sin(2 * np.pi * frequency * samples + pi)
wave2 = 10000 * np.sin(2 * np.pi * frequency * samples + pi)
# Convert it to wav format (16 bits)
wav_wave = np.array(wave, dtype=np.int16)
wav_wave2 = np.array(wave, dtype=np.int16)

wavfile.write('wave1.wav', sd.default.samplerate, wav_wave)
wavfile.write('wave2.wav', sd.default.samplerate, wav_wave2)
