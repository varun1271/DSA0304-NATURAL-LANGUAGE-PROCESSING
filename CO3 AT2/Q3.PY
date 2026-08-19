# Initial POS tags

tags = [
    ("economic", "JJ"),
    ("growth", "NN"),
    ("increases", "NNS"),
    ("employment", "NN")
]

print("Before Transformation:")
for word, tag in tags:
    print(word, "->", tag)

# Transformation rule:
# Change NNS to VBZ if previous word is NN

for i in range(1, len(tags)):
    if tags[i][1] == "NNS" and tags[i-1][1] == "NN":
        tags[i] = (tags[i][0], "VBZ")

print("\nAfter Transformation:")
for word, tag in tags:
    print(word, "->", tag)


# Word frequency

frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

print("\nWord Frequencies:")

for word, count in frequency.items():
    print(word, "->", count)

# Total frequency
total = sum(frequency.values())

print("\nTotal =", total)

# Probabilities
print("\nWord Probabilities:")

for word, count in frequency.items():
    probability = count / total
    print(word, "->", round(probability, 3))