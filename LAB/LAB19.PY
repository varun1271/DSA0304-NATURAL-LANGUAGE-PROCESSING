import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download("wordnet")
nltk.download("punkt")

sentence = "I went to the bank to deposit money"

# Tokenize the sentence
words = word_tokenize(sentence)

# Find the correct meaning of the word
sense = lesk(words, "bank")

print("Sentence:", sentence)

if sense:
    print("\nWord:", "bank")
    print("Sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")