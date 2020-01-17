# -*- coding: utf-8 -*-
"""

Numpy FFT example

Based on: 
    https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
    
"""

import numpy as np
import matplotlib.pyplot as plt

# Create sinusoidal data (two mixed signals)
time_points = np.linspace(0, 0.5, 500)  # seconds
f1 = 40  # Hz
f2 = 90  # Hz
amplitude1 = 1
amplitude2 = 0.5
signal = amplitude1 * np.sin(f1 * 2 * np.pi * time_points) + amplitude2 * np.sin(f2 * 2 * np.pi * time_points)

plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.plot(time_points, signal)
plt.show()

fft = np.fft.fft(signal)

# Second half of the fft result is the conjugate of the first half (because fft input is real, not complex)
# Hence, contains no additional information
for i in range(2):
    print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))
    
# Create array of frequency points
dt = time_points[1] - time_points[0]  # sampling interval 
N = signal.size
f = np.linspace(0, 1 / dt, N) # 1/dt = frequency

# Take first half of fft data:
f_half = f[:N // 2]
fft_half = np.abs(fft)[:N // 2]
fft_half = fft_half * 1 / N  # normalise

# Plot
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.bar(f_half, fft_half, width=1.5)
plt.show()
