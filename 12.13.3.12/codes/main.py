import numpy as np
from scipy.stats import bernoulli

# Number of simulations
num_simulations = 100000  # You can adjust this number based on your needs

# Initialize a list to store the results
results = []

# Simulate the process num_simulations times
for _ in range(num_simulations):
    # Simulate three coin tosses and count the number of tails (1 represents tails, 0 represents heads)
    coin_tosses = bernoulli.rvs(0.5, size=3)
    num_tails = np.sum(coin_tosses)
    results.append(num_tails)

# Calculate the variance
variance = np.var(results, ddof=1)

# Calculate the standard deviation
std_deviation = np.sqrt(variance)

# Print the results
print(f"Standard Deviation: {std_deviation}")

