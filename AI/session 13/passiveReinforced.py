import numpy as np

class GridWorld:
    def __init__(self, grid_size, start, goal, obstacles, policy):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.policy = policy
        self.values = np.zeros((grid_size, grid_size))
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor

    def is_valid(self, state):
        if (0 <= state[0] < self.grid_size) and (0 <= state[1] < self.grid_size):
            return state not in self.obstacles
        return False

    def step(self, state):
        action = self.policy[state[0], state[1]]
        next_state = (state[0] + action[0], state[1] + action[1])
        if not self.is_valid(next_state):
            next_state = state
        reward = 1 if next_state == self.goal else -0.01
        return next_state, reward

    def run_episode(self):
        state = self.start
        while state != self.goal:
            next_state, reward = self.step(state)
            self.values[state[0], state[1]] += self.alpha * (
                reward + self.gamma * self.values[next_state[0], next_state[1]] - self.values[state[0], state[1]]
            )
            state = next_state

    def train(self, episodes):
        for _ in range(episodes):
            self.run_episode()

    def print_values(self):
        for row in self.values:
            print(["{:.2f}".format(x) for x in row])

if __name__ == "__main__":
    grid_size = 5
    start = (0, 0)
    goal = (4, 4)
    obstacles = [(1, 1), (2, 2), (3, 3)]
    policy = np.array([[(0, 1), (0, 1), (0, 1), (0, 1), (1, 0)],
                       [(1, 0), (0, 0), (1, 0), (1, 0), (1, 0)],
                       [(1, 0), (1, 0), (0, 0), (1, 0), (1, 0)],
                       [(1, 0), (1, 0), (1, 0), (0, 0), (1, 0)],
                       [(1, 0), (1, 0), (1, 0), (1, 0), (0, 0)]])

    env = GridWorld(grid_size, start, goal, obstacles, policy)
    env.train(episodes=1000)
    env.print_values()
