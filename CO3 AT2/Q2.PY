# Penn Treebank POS Tags

sentence1 = {
    "Book": "VB",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB"
}

sentence2 = {
    "This": "DT",
    "book": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}

print("Sentence 1:")
for word, tag in sentence1.items():
    print(word, "->", tag)

print("\nSentence 2:")
for word, tag in sentence2.items():
    print(word, "->", tag)


# HMM probability

p_book_vb = 0.5 * 0.6
p_book_nn = 0.5 * 0.4

print("\nP(Book = VB) =", p_book_vb)
print("P(Book = NN) =", p_book_nn)

if p_book_vb > p_book_nn:
    print("HMM chooses VB")
else:
    print("HMM chooses NN")