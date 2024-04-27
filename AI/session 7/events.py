class Car:
  def __init__(self):
    self.speed = 0  # Current speed of the car
    self.stopped = False  # Flag to indicate if car is stopped
    self.traffic_light_color = None  # Current traffic light color (None, red, yellow, green)

  def drive(self):
    if not self.stopped:
      self.speed += 5  # Increase speed by 5 units (arbitrary)

  def handle_event(self, event):
    if event == "red_light":
      self.speed = 0
      self.stopped = True
      print("Car stopped at red light.")
    elif event == "green_light":
      self.stopped = False
      print("Car resumes driving.")
    elif event == "obstacle":
      self.speed = 0
      self.stopped = True
      print("Car stopped for obstacle.")
    else:
      print(f"Unknown event: {event}")

# Simulate events and car behavior
car = Car()

# Initial state (assume green light)
car.handle_event("green_light")
car.drive()
print(f"Car speed: {car.speed}")

# Traffic light turns red
car.handle_event("red_light")
print(f"Car speed: {car.speed}")

# Obstacle detected
car.handle_event("obstacle")
print(f"Car speed: {car.speed}")
