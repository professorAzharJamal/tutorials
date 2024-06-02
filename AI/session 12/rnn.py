import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generate synthetic dataset
def generate_sine_wave_data(num_samples, sequence_length):
    X = np.zeros((num_samples, sequence_length, 1))
    y = np.zeros((num_samples, 1))
    for i in range(num_samples):
        freq = np.random.uniform(0.1, 0.5)
        phase = np.random.uniform(0, np.pi)
        X[i, :, 0] = np.sin(np.linspace(0, 2 * np.pi * freq, sequence_length) + phase)
        y[i, 0] = 1 if freq > 0.3 else 0  # Label based on frequency
    return X, y

# Parameters
num_samples = 1000
sequence_length = 50

# Generate data
X, y = generate_sine_wave_data(num_samples, sequence_length)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the RNN model
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(sequence_length, 1)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model summary
model.summary()

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy}')

# Plot training and validation loss
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.show()

# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='val accuracy')
plt.legend()
plt.show()

# Predict on a few test samples
predictions = model.predict(X_test[:5])
print(f'Predictions: {predictions.flatten()}')
print(f'Actual labels: {y_test[:5].flatten()}')
