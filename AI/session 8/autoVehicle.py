import random

# Define a class for the autonomous vehicle
class AutonomousVehicle:
    def __init__(self, speed, lane, sensors):
        self.speed = speed  # Current speed (km/h)
        self.lane = lane  # Current lane (1 or 2)
        self.sensors = sensors  # Sensor data (e.g., distance to obstacles)

    def accelerate(self, amount):
        # Simulate acceleration within a safe limit
        self.speed = min(self.speed + amount, 120)  # Max speed 120 km/h

    def decelerate(self, amount):
        # Simulate deceleration within a safe limit
        self.speed = max(self.speed - amount, 0)  # Min speed 0 km/h

    def determine_lane(self):
        # Simulate lane selection based on speed
        if self.speed > 80:
            return 2  # Outer lane for high speeds
        else:
            return 1  # Inner lane for lower speeds

    def generate_sensor_data(self):
        # Simulate sensor data based on speed (e.g., higher speed leads to shorter detection range)
        front_obstacle_distance = random.randint(50 - self.speed, 100)
        rear_obstacle_distance = random.randint(20 - self.speed // 2, 50)
        return {'front': front_obstacle_distance, 'rear': rear_obstacle_distance}

# Example usage
current_speed = int(input("Enter current speed (km/h): "))
vehicle = AutonomousVehicle(current_speed, 1, {'front': 50, 'rear': 20})

# Simulate actions
vehicle.accelerate(10)
vehicle.decelerate(5)

# Determine lane based on speed
vehicle.lane = vehicle.determine_lane()

# Generate sensor data based on speed
vehicle.sensors = vehicle.generate_sensor_data()

print("Current speed:", vehicle.speed, "km/h")
print("Current lane:", vehicle.lane)
print("Sensor data:", vehicle.sensors)
