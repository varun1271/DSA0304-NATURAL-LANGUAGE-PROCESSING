from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["watches", "watching", "washable",
         "washer", "washed"]
for word in words:
    print(word, "->", ps.stem(word))
