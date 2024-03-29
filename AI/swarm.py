import numpy as np

class Particle:
    def __init__(self, dim, min_val, max_val):
        self.position = np.random.uniform(low=min_val, high=max_val, size=dim)
        self.velocity = np.random.uniform(low=-0.1, high=0.1, size=dim)
        self.best_position = self.position
        self.best_value = np.inf

    def update_position(self):
        self.position += self.velocity

    def update_velocity(self, global_best_position, w=0.5, c1=1, c2=1):
        r1 = np.random.rand(len(self.position))
        r2 = np.random.rand(len(self.position))

        self.velocity = w*self.velocity + c1*r1*(self.best_position - self.position) + c2*r2*(global_best_position - self.position)

class Swarm:
    def __init__(self, num_particles, dim, min_val, max_val):
        self.particles = [Particle(dim, min_val, max_val) for _ in range(num_particles)]
        self.global_best_position = None
        self.global_best_value = np.inf

    def optimize(self, objective_function, num_iterations):
        for _ in range(num_iterations):
            for particle in self.particles:
                value = objective_function(particle.position)
                if value < particle.best_value:
                    particle.best_position = particle.position
                    particle.best_value = value

                if value < self.global_best_value:
                    self.global_best_position = particle.position
                    self.global_best_value = value

            for particle in self.particles:
                particle.update_velocity(self.global_best_position)
                particle.update_position()


def objective_function(x):
    return np.sum(x**2)  # Minimize sum of squares


if __name__ == "__main__":
    num_particles = 20
    num_iterations = 100
    dim = 2
    min_val = -5
    max_val = 5

    swarm = Swarm(num_particles, dim, min_val, max_val)
    swarm.optimize(objective_function, num_iterations)

    print("Global Best Position:", swarm.global_best_position)
    print("Global Best Value:", swarm.global_best_value)
