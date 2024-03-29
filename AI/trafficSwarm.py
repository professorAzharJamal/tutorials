import numpy as np

class Vehicle:
    def __init__(self, id, position, velocity):
        self.id = id
        self.position = position
        self.velocity = velocity

    def update_position(self):
        self.position += self.velocity

class Intersection:
    def __init__(self, num_vehicles):
        self.vehicles = [Vehicle(id=i, position=np.random.rand(2)*100, velocity=np.random.rand(2)) for i in range(num_vehicles)]

    def update_traffic(self):
        for vehicle in self.vehicles:
            vehicle.update_position()
            # Add logic for collision avoidance and traffic management

    def print_status(self):
        for vehicle in self.vehicles:
            print(f"Vehicle {vehicle.id}: Position={vehicle.position}, Velocity={vehicle.velocity}")

if __name__ == "__main__":
    num_vehicles = 5
    intersection = Intersection(num_vehicles)

    print("Initial Vehicle Status:")
    intersection.print_status()

    num_iterations = 10
    for i in range(num_iterations):
        print(f"\nIteration {i+1}:")
        intersection.update_traffic()
        intersection.print_status()
