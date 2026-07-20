import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "player", "running", "happiness"]

print("Original Word\tStemmed Word")
print("-------------------------------")

for word in words:
    print(word, "\t\t", ps.stem(word))