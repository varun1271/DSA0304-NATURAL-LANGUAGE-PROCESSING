# Transformation-Based Tagging (Brill Tagger - Simple Version)

# Step 1: Initial tagging using simple rules (regex-based)
def initial_tag(words):
    tagged = []
    for w in words:
        if w.lower() in ["the", "a", "an"]:
            tagged.append((w, "DT"))
        elif w.lower() in ["dog", "cat", "boy", "girl", "car", "ball"]:
            tagged.append((w, "NN"))
        elif w.lower() in ["runs", "eats", "sleeps", "reads"]:
            tagged.append((w, "VBZ"))
        elif w.lower() in ["run", "eat", "sleep", "read"]:
            tagged.append((w, "VBP"))
        elif w.lower() in ["fast", "quickly", "slowly", "well"]:
            tagged.append((w, "RB"))
        elif w.lower() in ["fast", "quick", "good", "big"]:
            tagged.append((w, "JJ"))
        elif w.endswith("ing"):
            tagged.append((w, "VBG"))
        elif w.endswith("ed"):
            tagged.append((w, "VBD"))
        elif w.endswith("s"):
            tagged.append((w, "NNS"))
        else:
            tagged.append((w, "NN"))
    return tagged

# Step 2: Transformation rules
# Each rule: (condition, from_tag, to_tag)
# Rule 1: If a word is preceded by DT, change NN -> NNP (proper noun) - simple example
# Rule 2: If a word ends with 'ing', change tag to VBG (already handled, but example)
# Rule 3: If a word is followed by a noun, and current tag is JJ, keep JJ
# We'll apply a simple rule: If previous tag is DT and current is NN, keep NN
# Another rule: If word starts with capital letter, NN -> NNP

def apply_rules(tagged):
    for i in range(len(tagged)):
        word, tag = tagged[i]

        # Rule: Capitalized word that is NN becomes NNP
        if word[0].isupper() and tag == "NN":
            tagged[i] = (word, "NNP")

        # Rule: If previous word is DT and current is NNS, change to NN
        if i > 0 and tagged[i - 1][1] == "DT" and tag == "NNS":
            tagged[i] = (word, "NN")

    return tagged

sentence = input("Enter a sentence: ")
words = sentence.split()

tagged = initial_tag(words)
print("Initial Tags:", tagged)

final_tagged = apply_rules(tagged)
print("After Transformation Rules:", final_tagged)