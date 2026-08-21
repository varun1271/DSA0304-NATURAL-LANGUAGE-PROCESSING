import re

text = """
Natural language processing is useful.
Natural language processing helps computers understand language.
Language is used for communication.
"""

sentences = [
    sentence.strip().lower()
    for sentence in text.strip().split(".")
    if sentence.strip()
]

print("Text Coherence Analysis:\n")

total_score = 0

for i in range(len(sentences) - 1):

    words1 = set(re.findall(r"\w+", sentences[i]))
    words2 = set(re.findall(r"\w+", sentences[i + 1]))

    common_words = words1.intersection(words2)

    print("Sentence", i + 1, "and Sentence", i + 2)
    print("Common words:", common_words)

    score = len(common_words)
    print("Coherence score:", score)
    print()

    total_score += score

print("Total Coherence Score:", total_score)

if total_score > 0:
    print("The text is coherent.")
else:
    print("The text has low coherence.")