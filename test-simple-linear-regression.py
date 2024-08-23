import numpy as np
import matplotlib.pyplot as plt

def plot_sin(x):
    y = np.sin(x)
    plt.plot(x, y)

def plot_cos(x):
    y = np.cos(x)
    plt.plot(x,y)

x = np.arange(0, 2*np.pi, 0.001)

plot_sin(x)
plot_cos(x)


plt.show()

