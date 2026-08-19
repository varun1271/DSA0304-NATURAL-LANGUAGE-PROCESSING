import re
from collections import Counter

corpus = """
The student is reading a book.
The student is writing a note.
The student is learning Python.
The teacher is teaching the student.
The teacher is reading a book.
The student likes Python.
"""

sentences = corpus.lower().split(".")
sentences = [re.findall(r'\b\w+\b', s) for s in sentences if s.strip()]

unigram = Counter()
bigram = Counter()
trigram = Counter()

for s in sentences:
    unigram.update(s)

    for i in range(len(s)-1):
        bigram[(s[i], s[i+1])] += 1

    for i in range(len(s)-2):
        trigram[(s[i], s[i+1], s[i+2])] += 1

total_words = sum(unigram.values())

# Unigram probability
def unigram_prob(word):
    return unigram[word] / total_words

# Bigram probability
def bigram_prob(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]

# Trigram probability
def trigram_prob(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]

# Backoff model
def backoff(w1, w2, w3):
    p = trigram_prob(w1, w2, w3)

    if p > 0:
        return p

    p = bigram_prob(w2, w3)

    if p > 0:
        return p

    return unigram_prob(w3)

# Deleted Interpolation
def interpolation(w1, w2, w3):
    p1 = unigram_prob(w3)
    p2 = bigram_prob(w2, w3)
    p3 = trigram_prob(w1, w2, w3)

    # Simple interpolation weights
    l1 = 0.2
    l2 = 0.3
    l3 = 0.5

    return l1*p1 + l2*p2 + l3*p3


# Prediction
def predict(sentence, model):
    words = sentence.lower().split()
    results = []

    for word in unigram:
        if len(words) >= 2:
            if model == "unsmoothed":
                p = trigram_prob(words[-2], words[-1], word)

            elif model == "backoff":
                p = backoff(words[-2], words[-1], word)

            else:
                p = interpolation(words[-2], words[-1], word)

        results.append((word, p))

    return sorted(results, key=lambda x: x[1], reverse=True)[:5]


sentence = input("Enter sentence: ")

for model in ["unsmoothed", "backoff", "interpolation"]:
    print("\n", model.upper())

    for word, p in predict(sentence, model):
        print(word, "->", round(p, 4))