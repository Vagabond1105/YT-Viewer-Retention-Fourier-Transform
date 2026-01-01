# this is the waveform fourier decomposition file

import numpy as np

def fourier_transform(signal, dt=1.0):
    signal = signal - np.mean(signal)  # remove DC offset only

    fft_vals = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=dt)

    magnitude = np.abs(fft_vals)

    return freqs, magnitude
