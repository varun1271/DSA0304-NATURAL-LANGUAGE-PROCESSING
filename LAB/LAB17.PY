import nltk
from nltk.corpus import wordnet

# Download WordNet data
nltk.download("wordnet")

word = "bank"

# Get all synsets of the word
synsets = wordnet.synsets(word)

print("Word:", word)
print("\nSynsets:")

for synset in synsets:
    print("\nName:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())