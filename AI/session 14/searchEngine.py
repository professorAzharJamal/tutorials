from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Never jump over the lazy dog quickly.",
    "A quick brown dog outpaces a quick fox.",
    "The quick brown fox is quick and the dog is lazy."
]

# Preprocess and vectorize documents using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Search function
def search(query, tfidf_matrix, vectorizer):
    # Vectorize the query
    query_vec = vectorizer.transform([query])
    # Calculate cosine similarity between query and documents
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    # Get top document indices based on similarity scores
    top_indices = cosine_similarities.argsort()[-5:][::-1]
    return [(index, cosine_similarities[index]) for index in top_indices]

# Example search query
query = "quick fox"
results = search(query, tfidf_matrix, vectorizer)

# Display search results
for index, score in results:
    print(f"Document {index} (Score: {score}): {documents[index]}")
