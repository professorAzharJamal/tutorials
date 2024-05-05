import nltk
from nltk.chunk import conlltags2tree, tree2conlltags

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Sample text
text = "This is a simple sentence for NLP demonstration."

# Tokenization: Splitting the text into words
tokens = nltk.word_tokenize(text)
print("Tokenized words:", tokens)

# Part-of-Speech (POS) Tagging: Identifying the grammatical role of each word
pos_tags = nltk.pos_tag(tokens)
print("POS tags:", pos_tags)

# Stop Word Removal: Removing common words with little meaning
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
filtered_tokens = [word for word in tokens if word not in stop_words]
print("Filtered tokens (without stop words):", filtered_tokens)

# Named Entity Recognition (NER): Identifying named entities
pos_tagged_with_chunk = [(word, pos_tag, 'O') for word, pos_tag in nltk.pos_tag(tokens)]  # Include chunk tags
ner_tags = conlltags2tree(pos_tagged_with_chunk)
print("Named Entity Recognition:", tree2conlltags(ner_tags))