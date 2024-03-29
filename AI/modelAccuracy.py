# True labels (spam or not spam) for 10 emails
true_labels = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]

# Predicted labels (spam or not spam) by the model
predicted_labels = [0, 1, 0, 0, 1, 1, 0, 1, 1, 1]

# Function to calculate the number of correct predictions
def calculate_accuracy(true_labels, predicted_labels):
  correct_predictions = 0
  for i in range(len(true_labels)):
    if true_labels[i] == predicted_labels[i]:
      correct_predictions += 1
  return correct_predictions

# Calculate the number of correct predictions
number_correct = calculate_accuracy(true_labels, predicted_labels)

# Calculate the total number of test samples
total_samples = len(true_labels)

# Calculate the accuracy
accuracy = number_correct / total_samples

# Print the accuracy as a percentage
print("Accuracy:", accuracy * 100, "%")
