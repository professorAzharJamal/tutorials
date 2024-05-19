import tensorflow as tf
from tensorflow.keras import layers, models, callbacks, regularizers
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the model with additional layers, regularization, and dropout
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Input layer
    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.001)),  # Hidden layer with L2 regularization
    layers.Dropout(0.5),  # Dropout layer for regularization
    layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)),  # Another hidden layer
    layers.Dropout(0.5),  # Another dropout layer
    layers.Dense(10, activation='softmax')  # Output layer
])

# Compile the model with additional configurations
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Add early stopping callback to prevent overfitting
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Train the model with validation split and early stopping
history = model.fit(x_train, y_train, epochs=50, batch_size=128, validation_split=0.2, callbacks=[early_stopping])

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Plot training and validation accuracy and loss over epochs
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Predict using the model and display the first 5 test images, their predicted labels, and the true labels
predictions = model.predict(x_test)
for i in range(5):
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.title(f"Prediction: {tf.argmax(predictions[i])}, True: {y_test[i]}")
    plt.show()
