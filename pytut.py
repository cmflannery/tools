import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-50, 50)
y = x**2

with plt.xkcd():
    plt.plot(x, y)
    plt.show()
