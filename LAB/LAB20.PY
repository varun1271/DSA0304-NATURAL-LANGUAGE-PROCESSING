from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# List of documents
documents = [
    "Natural language processing is a branch of artificial intelligence",
    "Machine learning is used in artificial intelligence",
    "Python is widely used for natural language processing",
    "Information retrieval helps find relevant documents"
]

# Get search query from user
query = input("Enter your search query: ")

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert query into TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate cosine similarity
similarity_scores = cosine_similarity(
    query_vector, tfidf_matrix
).flatten()

# Rank documents from highest to lowest score
ranked_documents = sorted(
    enumerate(similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

print("\nDocument Ranking:\n")

for index, score in ranked_documents:
    print("Rank:", ranked_documents.index((index, score)) + 1)
    print("Score:", round(score, 3))
    print("Document:", documents[index])
    print()