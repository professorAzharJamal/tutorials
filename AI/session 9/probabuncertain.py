import random

# Define the bias (probability of heads)
bias = 0.3

# Simulate a coin flip
def flip_coin():
  return "heads" if random.random() < bias else "tails"

# Perform multiple flips and calculate probability of heads
num_flips = 1000
heads_count = sum(flip_coin() == "heads" for _ in range(num_flips))
probability_heads = heads_count / num_flips

print(f"Probability of heads in {num_flips} flips: {probability_heads:.4f}")
