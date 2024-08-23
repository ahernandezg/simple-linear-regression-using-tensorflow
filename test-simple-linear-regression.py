import numpy as np
import matplotlib.pyplot as plt

def plot_sin(x,y):
    plt.plot(x, y)
    
x = np.arange(0, 2*np.pi, 0.001)
y = np.sin(x)

plot_sin(x,y)
plt.show()

