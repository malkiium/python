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
x = np.linspace(0, 20, 1000)  # 1000 points between 0 and 20

# Complex y-axis data combining several functions
y1 = np.sin(x)               # Sine wave
y2 = np.cos(2 * x)          # Cosine wave with double frequency
y3 = 0.5 * np.sin(0.5 * x)  # Low-frequency sine wave
y4 = np.exp(-0.1 * x) * np.sin(5 * x)  # Damped sine wave
y5 = 0.1 * np.random.normal(size=x.shape)  # Random noise

# Combine all the data
y = y1 + y2 + y3 + y4 + y5

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