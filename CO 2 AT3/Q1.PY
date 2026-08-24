from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["infection", "infectious", "infected", "infect"]

for word in words:
    print(word, "->", ps.stem(word))
