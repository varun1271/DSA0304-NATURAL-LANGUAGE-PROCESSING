# Voice assistant parsing

sentence = "book a flight to Delhi with a window seat"

print("Input:", sentence)

print("\nTop-Down Parsing:")
print("Starting from Sentence (S)")
print("S -> Verb + Object + Details")
print("Backtracking may be required for ambiguous parts.")

print("\nPossible interpretations:")
print("1. Book a flight to Delhi.")
print("2. Book a flight with a window seat.")
print("3. Book a flight to Delhi with a window seat.")

print("\nEarley Parsing:")
print("Handles multiple interpretations.")
print("Handles incomplete input.")
print("Uses dynamic programming.")
print("Suitable for real-time voice assistants.")

print("\nComparison:")
print("Top-Down Parser -> More backtracking")
print("Earley Parser   -> Better ambiguity handling")