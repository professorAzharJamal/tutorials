import random

# Define game environment
class Environment:
  def __init__(self):
    self.state = 0  # Current position (0 to 4)
    self.rewards = {0: 0, 1: 2, 2: 10, 3: -1, 4: 0}  # Rewards for each state

  def act(self, action):  # Perform action and update state
    if action == "L":
      self.state = max(self.state - 1, 0)  # Move left (stay within bounds)
    elif action == "R":
      self.state = min(self.state + 1, 4)  # Move right (stay within bounds)
    return self.rewards[self.state]  # Return reward for the new state

# Q-Learning Agent
class Agent:
  def __init__(self, alpha=0.1, gamma=0.9):
    self.alpha = alpha  # Learning rate
    self.gamma = gamma  # Discount factor
    self.Q = {}  # Q-value table (state, action): Q-value

  def choose_action(self, state, epsilon=0.1):
    # Explore with probability epsilon, exploit with 1-epsilon
    if random.random() < epsilon:
      return random.choice(["L", "R"])  # Random action
    else:
      # Choose action with highest Q-value
      return max(self.Q.get((state, action), 0) for action in ["L", "R"])

  def learn(self, state, action, reward, next_state):
    # Update Q-value based on Bellman equation
    Q_sa = self.Q.get((state, action), 0)  # Current Q-value
    Q_sa_prime = max(self.Q.get((next_state, a), 0) for a in ["L", "R"])  # Max Q-value for next state
    self.Q[(state, action)] = Q_sa + self.alpha * (reward + self.gamma * Q_sa_prime - Q_sa)

# Main Function
def main():
  env = Environment()
  agent = Agent()
  num_episodes = 1000  # Number of training episodes

  for episode in range(num_episodes):
    state = env.state
    while True:
      # Choose action based on Q-value table with exploration
      action = agent.choose_action(state)
      # Take action, receive reward, and observe next state
      reward = env.act(action)
      next_state = env.state
      # Update Q-value table based on experience
      agent.learn(state, action, reward, next_state)
      state = next_state

      # Check for terminal state (reaching boundary)
      if state == 0 or state == 4:
        break

  # Print learned policy (action with highest Q-value for each state)
  for state in range(5):
    print(f"State {state}: Best Action: {agent.choose_action(state, epsilon=0)}")

if __name__ == "__main__":
  main()
