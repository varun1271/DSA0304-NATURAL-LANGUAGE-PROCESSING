import re

sentence = "The intelligent student reads the book in the library"

# Simple list of common nouns
nouns = {
    "student": "a person who studies",
    "book": "a collection of written pages",
    "library": "a place containing books"
}

# Find noun phrases: adjective/article followed by a noun
words = sentence.lower().split()

print("Sentence:", sentence)
print("\nNoun Phrases and Meanings:\n")

for word in words:
    if word in nouns:
        print("Noun Phrase:", word)
        print("Meaning:", nouns[word])
        print()