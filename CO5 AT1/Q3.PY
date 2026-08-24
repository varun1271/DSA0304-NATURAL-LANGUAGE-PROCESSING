# Constraint-Based Word Sense Disambiguation

sentence = (
    "The bank by the river flooded after the storm, "
    "but it was saved by quick action."
)

# Possible meanings of bank
meanings = [
    "financial institution",
    "riverbank"
]

# Context words
context = ["river", "flooded", "storm"]

# Select correct meaning
if "river" in context and "flooded" in context:
    correct_sense = "riverbank"
else:
    correct_sense = "financial institution"

print("Source Sentence:")
print(sentence)

print("\nPossible Meanings:")
for meaning in meanings:
    print("-", meaning)

print("\nCorrect Word Sense:")
print("bank ->", correct_sense)


# Predicate logic representation
print("\nPredicate Logic Representation:")

logic = [
    "riverbank(bank)",
    "location(bank, river)",
    "storm(storm1)",
    "flood(bank)",
    "after(flood, storm1)",
    "quick_action(action1)",
    "saved_by(bank, action1)"
]

for statement in logic:
    print(statement)


# Target sentence
target = (
    "The riverbank was flooded after the storm, "
    "but quick action saved it."
)

print("\nTarget Sentence:")
print(target)


# Simple RST-style discourse tree
print("\nDiscourse Tree:")
print("""
              CONTRAST
             /        \\
      NUCLEUS          SATELLITE
         |                |
  Bank was flooded    Bank was saved
  after the storm     by quick action
""")