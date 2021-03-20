import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(5,10)
y = x ** 2
plt.plot(x,y,'b')
plt.xlabel('Values of x')
plt.ylabel('sq of x values')
plt.title('Title')
plt.show()