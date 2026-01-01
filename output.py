# this is the signal analytics output file

import matplotlib.pyplot as plt

def plot_results(t, price, freqs, magnitude):
    plt.figure(figsize=(12,4))
    plt.plot(t, price)
    plt.xlabel("Time (days)")
    plt.ylabel("Price")
    plt.title("Share Price vs Time")
    plt.show()

    plt.figure(figsize=(12,4))
    plt.plot(freqs[freqs > 0], magnitude[freqs > 0])
    plt.xlabel("Frequency (1/day)")
    plt.ylabel("Magnitude")
    plt.title("Fourier Spectrum of Share Price")
    plt.show()
