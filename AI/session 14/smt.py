import random  # Import the random module

# Sample English and French sentences
english_sentence = "The cat sat on the mat."
french_sentence = "Le chat est assis sur le tapis."

# Split sentences into words
english_words = english_sentence.lower().split()  # Lowercase and split
french_words = french_sentence.lower().split()

# Create an empty dictionary to store word alignments (English:French)
word_alignments = {}

# Iterate through both sentences (assuming same length for simplicity)
for i in range(len(english_words)):
  # Randomly assign an alignment with a small chance of skipping
  if random.random() < 0.8:  # 80% chance of alignment
    word_alignments[english_words[i]] = french_words[i]
  else:
    word_alignments[english_words[i]] = None  # Skip alignment

# Print the aligned words
print("English:", english_words)
print("French:", french_words)
print("Alignments:", word_alignments)

# Calculate a very basic translation probability (assuming aligned words have 100% probability)
translation_probability = 1.0
for english_word, french_word in word_alignments.items():
  if french_word:  # Consider only aligned words
    translation_probability *= 0.8  # Probability of translating a word correctly (adjustable)

print("Translation Probability:", translation_probability)
