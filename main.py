# this file calls the modules and runs the program basically

from input import load_price
from processing import fourier_transform
from output import plot_results

t, price = load_price("^GSPC", "5y")
freqs, magnitude = fourier_transform(price)
plot_results(t, price, freqs, magnitude)