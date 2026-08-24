from nltk.stem import PorterStemmer, WordNetLemmatizer
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words = ["organization", "organizer",
         "organizing", "organized"]
print("Original -> Stem -> Lemma")
for word in words:
    stem = ps.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(word, "->", stem, "->", lemma)
