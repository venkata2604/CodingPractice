import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation
mu, sigma = 0, 0.1

# Create a numpy array of x-values
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

# Calculate the probability density function (pdf) for each x-value
y = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu)/sigma)**2)

# Plot the normal distribution curve
plt.plot(x, y)
plt.title(f'Normal Distribution Curve with Sigma = {sigma}')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.show()
