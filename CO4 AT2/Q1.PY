# Simple CFG analysis

sentence = "show me the transactions with the card from last month"

words = sentence.split()

print("Input:", sentence)

print("\nWords:")
for word in words:
    print(word)

# Possible meanings
print("\nPossible Interpretations:")

print("1. Transactions were made using the card.")
print("2. Transactions are related to the card.")

# Simple feature agreement example
subject = "customer"
verb = "show"

if subject == "customer" and verb == "show":
    print("\nSubject-Verb Agreement: Correct")

# Simple parsing method
print("\nImproved Parser: Earley Parser")
print("Reason: Handles ambiguity and long sentences efficiently.")