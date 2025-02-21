'''import matplotlib.pyplot as plt # type: ignore

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Simple plot')
plt.xlabel('years')
plt.ylabel('values')
plt.show()'''


import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Generate more complex data
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)  # Sine wave with noise

# Create the plot
plt.plot(x, y, label='Sine wave with noise', color='blue')

# Adding more fun with some extra curves
y2 = np.cos(x)  # Cosine wave
plt.plot(x, y2, label='Cosine wave', color='red', linestyle='dashed')

# Adding titles and labels
plt.title('Complex and Fun Plot')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()  # Show the legend
plt.grid()  # Add a grid for better readability
plt.show()