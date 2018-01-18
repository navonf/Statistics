import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Normal Distribution aka the Gaussian Distribution.
mu, sigma = 0, 1

plt.figure(1)
plt.subplot(221)
samples = np.random.normal(mu, sigma, 100)
