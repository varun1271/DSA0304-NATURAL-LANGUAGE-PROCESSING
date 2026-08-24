from nltk.stem import PorterStemmer

ps = PorterStemmer()

# Sample BBC-style news articles
data = [
    "The organization is organizing a new event",
    "The organizer organized the meeting",
    "Researchers are studying new technology",
    "The company is developing new products",
    "The government announced new policies"
]

# Function to stem complete sentences
def stem_text(text):
    words = text.split()
    return " ".join(ps.stem(word) for word in words)

# Compare original and stemmed articles
print("ARTICLE ANALYSIS\n")

for text in data:
    print("Original :", text)
    print("Stemmed  :", stem_text(text))
    print()
