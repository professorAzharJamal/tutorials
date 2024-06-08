import numpy as np

class GridWorld:
    def __init__(self, grid_size, start, goal, obstacles):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.q_table = np.zeros((grid_size, grid_size, 4))
        self.actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        self.epsilon = 0.1  # Exploration rate
        self.alpha = 0.1    # Learning rate
        self.gamma = 0.9    # Discount factor

    def is_valid(self, state):
        if (0 <= state[0] < self.grid_size) and (0 <= state[1] < self.grid_size):
            return state not in self.obstacles
        return False

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(4)  # Explore: random action
        else:
            return np.argmax(self.q_table[state[0], state[1]])  # Exploit: best action

    def step(self, state, action):
        next_state = (state[0] + self.actions[action][0], state[1] + self.actions[action][1])
        if not self.is_valid(next_state):
            next_state = state
        reward = 1 if next_state == self.goal else -0.01
        return next_state, reward

    def train(self, episodes):
        for episode in range(episodes):
            state = self.start
            while state != self.goal:
                action = self.select_action(state)
                next_state, reward = self.step(state, action)
                best_next_action = np.argmax(self.q_table[next_state[0], next_state[1]])
                td_target = reward + self.gamma * self.q_table[next_state[0], next_state[1], best_next_action]
                td_error = td_target - self.q_table[state[0], state[1], action]
                self.q_table[state[0], state[1], action] += self.alpha * td_error
                state = next_state

    def print_policy(self):
        policy = np.full((self.grid_size, self.grid_size), ' ')
        policy[self.goal] = 'G'
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) in self.obstacles or (i, j) == self.goal:
                    continue
                best_action = np.argmax(self.q_table[i, j])
                policy[i, j] = '↑→↓←'[best_action]
        print(policy)

if __name__ == "__main__":
    grid_size = 5
    start = (0, 0)
    goal = (4, 4)
    obstacles = [(1, 1), (2, 2), (3, 3)]
    env = GridWorld(grid_size, start, goal, obstacles)
    env.train(episodes=1000)
    env.print_policy()
