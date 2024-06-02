import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Input data (4 samples with 3 features each)
X = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])

# Output data (4 samples with 1 output each)
y = np.array([[0],
              [1],
              [1],
              [0]])

# Create the model
model = Sequential()
model.add(Dense(4, input_dim=3, activation='sigmoid'))  # Hidden layer with 4 neurons
model.add(Dense(1, activation='sigmoid'))  # Output layer with 1 neuron

# Compile the model
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10000, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)
print(f"Model accuracy: {accuracy}")

# Make predictions
predictions = model.predict(X)
print("Predictions after training:")
print(predictions)
