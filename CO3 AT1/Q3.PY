import re
import math
from collections import Counter

# Training corpus
train = """
The student is reading a book.
The student is writing a note.
The teacher is reading a book.
The teacher is teaching the student.
"""

# Test corpus
test = """
The student is reading.
The teacher is teaching.
"""

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

train_words = tokenize(train)
test_words = tokenize(test)

unigram = Counter(train_words)
bigram = Counter(zip(train_words, train_words[1:]))
trigram = Counter(zip(train_words, train_words[1:], train_words[2:]))

# Probabilities
def uni_prob(word):
    return unigram[word] / len(train_words)

def bi_prob(w1, w2):
    count = unigram[w1]

    if count == 0:
        return 0

    return bigram[(w1, w2)] / count

def tri_prob(w1, w2, w3):
    count = bigram[(w1, w2)]

    if count == 0:
        return 0

    return trigram[(w1, w2, w3)] / count


# Entropy calculation
def entropy(probabilities):
    total = 0
    count = 0

    for p in probabilities:
        if p > 0:
            total += -math.log2(p)
            count += 1

    return total / count if count > 0 else 0


# Unigram entropy
uni_probs = [uni_prob(w) for w in test_words]

# Bigram entropy
bi_probs = []

for i in range(len(test_words)-1):
    bi_probs.append(
        bi_prob(test_words[i], test_words[i+1])
    )

# Trigram entropy
tri_probs = []

for i in range(len(test_words)-2):
    tri_probs.append(
        tri_prob(
            test_words[i],
            test_words[i+1],
            test_words[i+2]
        )
    )

print("Unigram Entropy:", round(entropy(uni_probs), 4))
print("Bigram Entropy:", round(entropy(bi_probs), 4))
print("Trigram Entropy:", round(entropy(tri_probs), 4))