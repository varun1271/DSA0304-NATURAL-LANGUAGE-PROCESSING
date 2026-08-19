# Sentence
sentence = "The student reads a book."

print("Sentence:", sentence)

# CFG representation
print("\nCFG Tree:")
print("S")
print("|-- NP")
print("|   |-- The")
print("|   `-- student")
print("`-- VP")
print("    |-- reads")
print("    `-- NP")
print("        |-- a")
print("        `-- book")

# Dependency representation
print("\nDependency Structure:")
print("reads -> student")
print("student -> The")
print("reads -> book")
print("book -> a")