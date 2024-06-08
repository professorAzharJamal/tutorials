import numpy as np

class MultiArmedBandit:
    def __init__(self, k):
        self.k = k
        self.q_true = np.random.randn(k)
        self.q_estimated = np.zeros(k)
        self.action_count = np.zeros(k)
        self.epsilon = 0.1

    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.k)
        else:
            return np.argmax(self.q_estimated)

    def take_action(self, action):
        reward = np.random.randn() + self.q_true[action]
        self.action_count[action] += 1
        self.q_estimated[action] += (reward - self.q_estimated[action]) / self.action_count[action]
        return reward

    def run(self, steps):
        rewards = np.zeros(steps)
        for step in range(steps):
            action = self.select_action()
            reward = self.take_action(action)
            rewards[step] = reward
        return rewards

if __name__ == "__main__":
    bandit = MultiArmedBandit(k=10)
    rewards = bandit.run(steps=1000)
    print(f"Average reward: {np.mean(rewards)}")
