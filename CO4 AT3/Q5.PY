sentence = "The student reads a book."

print("Sentence:", sentence)

# Transition-based parsing
print("\nTransition-Based Parsing:")
print("SHIFT -> The")
print("SHIFT -> student")
print("RIGHT-ARC -> student")
print("SHIFT -> reads")
print("RIGHT-ARC -> reads")
print("SHIFT -> book")
print("RIGHT-ARC -> book")

# Graph-based parsing
print("\nGraph-Based Parsing:")
print("Create possible dependency relationships")
print("Compare possible structures")
print("Select the best dependency tree")

print("\nComparison:")
print("Transition-Based -> Fast and memory efficient")
print("Graph-Based -> Considers global structure")

print("\nConclusion:")
print("Transition-Based parsing is better for large-scale applications.")