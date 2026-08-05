# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        kind = "Inflectional"
        normalized = "connect"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        kind = "Inflectional"
        normalized = "connect"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        kind = "Derivational"
        normalized = "connect"

    print("-" * 50)
    print("Word       :", word)
    print("Root       :", root)
    print("Suffix     :", suffix)
    print("Type       :", kind)
    print("Normalized :", normalized)