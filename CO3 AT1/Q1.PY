from collections import Counter

# Simple corpus
text = """
the student is reading
the student is writing
the student is learning
the teacher is teaching
the teacher is reading
"""

# Tokenize
words = text.lower().split()

# Create counts
unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
trigram = Counter(zip(words, words[1:], words[2:]))

# Choose N
n = int(input("Enter N (1, 2 or 3): "))

# Display counts
if n == 1:
    print("\nUnigram Counts:")
    print(unigram)

elif n == 2:
    print("\nBigram Counts:")
    print(bigram)

elif n == 3:
    print("\nTrigram Counts:")
    print(trigram)

# Input sentence
sentence = input("\nEnter sentence: ").lower().split()

# Find next words
last = sentence[-1]
previous = sentence[-2] if len(sentence) > 1 else ""

result = []

for word in unigram:

    if n == 1:
        probability = unigram[word] / len(words)

    elif n == 2:
        count = bigram[(last, word)]

        if unigram[last] > 0:
            probability = count / unigram[last]
        else:
            probability = 0

    else:
        count = trigram[(previous, last, word)]

        if bigram[(previous, last)] > 0:
            probability = count / bigram[(previous, last)]
        else:
            probability = 0

    result.append((word, probability))

# Sort by probability
result.sort(key=lambda x: x[1], reverse=True)

print("\nTop 5 Next Words:")

for word, probability in result[:5]:
    print(word, "=", round(probability, 3))

# Unseen N-gram
print("\nUnseen N-gram example:")

if n == 2:
    print("student eats =", bigram[("student", "eats")])

elif n == 3:
    print("student is eating =", trigram[("student", "is", "eating")])