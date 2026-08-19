from collections import Counter
import math

text = """
data science is powerful
data science drives innovation
data science is evolving
"""

words = text.lower().split()

unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
trigram = Counter(zip(words, words[1:], words[2:]))

# 1. MLE P(science | data)
p = bigram[("data", "science")] / unigram["data"]

print("P(science | data) =", p)

# 2. Backoff for "data science improves"
if trigram[("data", "science", "improves")] > 0:
    p2 = trigram[("data", "science", "improves")] / bigram[("data", "science")]
elif bigram[("science", "improves")] > 0:
    p2 = bigram[("science", "improves")] / unigram["science"]
elif unigram["improves"] > 0:
    p2 = unigram["improves"] / len(words)
else:
    p2 = 0

print("P(improves | data science) =", p2)

# 3. Deleted Interpolation
tri = 2 / 3
bi = 2 / 3
uni = unigram["is"] / len(words)

final = (0.5 * tri) + (0.3 * bi) + (0.2 * uni)

print("Interpolated probability =", round(final, 4))

# 4. Entropy
p1 = 0.66
p2 = 0.33

entropy = -(p1 * math.log2(p1) + p2 * math.log2(p2))

print("Entropy =", round(entropy, 4))