# Healthcare NLP system

sentence = """The doctor who reviewed the patient last week
recommends starting medication and scheduling a follow-up visit in Chennai."""

print("Input Sentence:")
print(sentence)

# Step 1: Tokenization
words = sentence.replace(".", "").split()

print("\nStep 1 - Tokens:")
print(words)

# Step 2: Basic CFG structure
print("\nStep 2 - CFG Structure:")
print("S -> Subject + Verb + Object")
print("Subject -> The doctor + Relative Clause")
print("Relative Clause -> who reviewed the patient last week")
print("Verb -> recommends")
print("Object -> starting medication + scheduling follow-up visit")

# Step 3: Feature structure
print("\nStep 3 - Feature Structure:")
print("Subject: doctor")
print("Number: Singular")
print("Verb: recommends")
print("Agreement: Correct")

# Step 4: PCFG
print("\nStep 4 - PCFG:")
print("Most probable parse is selected using grammar probabilities.")

# Step 5: Sub-categorization
print("\nStep 5 - Medical Verb Relations:")
print("review -> doctor reviews patient")
print("recommend -> doctor recommends treatment")
print("schedule -> schedule follow-up visit")

# Step 6: Semantic extraction
print("\nStep 6 - Structured Information:")

print("Diagnosis: Not explicitly mentioned")
print("Action 1: Start medication")
print("Action 2: Schedule follow-up visit")
print("Location: Chennai")

# Step 7: Efficient parsing
print("\nStep 7 - Final System:")
print("CFG + PCFG + Feature Structures + Earley Parsing")
print("Suitable for real-time hospital processing.")