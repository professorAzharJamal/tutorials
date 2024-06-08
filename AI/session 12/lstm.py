import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Generate a simple sequential dataset
def create_dataset(seq_length, total_samples):
    X = []
    y = []
    for _ in range(total_samples):
        start = np.random.randint(0, 100)
        seq = np.array([i for i in range(start, start + seq_length + 1)])
        X.append(seq[:-1])
        y.append(seq[-1])
    return np.array(X), np.array(y)

# Create the dataset
seq_length = 10
total_samples = 1000
X, y = create_dataset(seq_length, total_samples)

# Reshape the input to be [samples, time steps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# Define the LSTM model
model = models.Sequential([
    layers.LSTM(50, activation='relu', input_shape=(seq_length, 1)),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, y, epochs=200, batch_size=32, validation_split=0.2)

# Predict on new data
test_seq = np.array([i for i in range(100, 110)]).reshape((1, seq_length, 1))
predicted = model.predict(test_seq)
print(f"Predicted next value: {predicted}")
