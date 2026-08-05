# Stemming-Based Preprocessing

words = ["played", "player", "playing"]

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        kind = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        kind = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        kind = "Derivational"

    print("-" * 50)
    print("Word :", word)
    print("Stem :", stem)
    print("Removed Affix :", affix)
    print("Type :", kind)
    print("Normalized :", "play")