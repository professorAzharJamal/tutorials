from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Hyperparameters (adjust as needed)
max_words = 5000  # Maximum number of words to consider
max_len = 200  # Maximum sequence length for padding
embedding_dim = 128  # Embedding dimension for word representation
lstm_units = 64  # Number of units in the LSTM layer

# Load IMDB movie reviews dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=max_words)

# Pad sequences to a fixed length
train_data = pad_sequences(train_data, maxlen=max_len)
test_data = pad_sequences(test_data, maxlen=max_len)

# Define the RNN model
model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=max_len))
model.add(LSTM(lstm_units))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model (replace with your training loop)
model.fit(train_data, train_labels, epochs=10, batch_size=32)  # Adjust epochs and batch size

# Evaluate on test data (assuming binary classification)
test_loss, test_acc = model.evaluate(test_data, test_labels)
print("Test Accuracy:", test_acc)

# Make prediction on a new review (replace with your review text)
new_review = "This movie was fantastic!"
new_review = pad_sequences([imdb.text_to_index(word) for word in new_review.split()], maxlen=max_len)
prediction = model.predict(new_review)
predicted_class = int(prediction[0][0] > 0.5)  # Threshold for positive sentiment

if predicted_class == 1:
  print("Review predicted as positive.")
else:
  print("Review predicted as negative.")
