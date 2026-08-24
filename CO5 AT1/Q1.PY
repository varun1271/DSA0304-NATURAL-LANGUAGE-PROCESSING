# Constraint-Based Coreference Resolution

paragraph = (
    "John and Mary went to the park. "
    "He brought a ball. "
    "She wanted to play with it. "
    "The dog chased him excitedly. "
    "Finally, they all went home."
)

# Mentions and possible antecedents
mentions = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["John", "Mary", "ball"],
    "him": ["John", "Mary", "dog"],
    "they": ["John and Mary", "John", "Mary", "dog"]
}

# Simple constraint resolution
resolved = {
    "He": "John",          # Gender constraint
    "She": "Mary",         # Gender constraint
    "it": "ball",          # Semantic compatibility
    "him": "John",         # Gender + coherence
    "they": "John and Mary"  # Number constraint
}

print("Paragraph:")
print(paragraph)

print("\nMentions and Possible Antecedents:")
for mention, candidates in mentions.items():
    print(mention, "->", candidates)

print("\nFinal Resolution:")
for mention, antecedent in resolved.items():
    print(mention, "->", antecedent)

# Rewrite paragraph
rewritten = (
    "John and Mary went to the park. "
    "John brought a ball. "
    "Mary wanted to play with the ball. "
    "The dog chased John excitedly. "
    "Finally, John and Mary all went home."
)

print("\nResolved Paragraph:")
print(rewritten)