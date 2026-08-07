words = ["govern", "government", "governance"]

for word in words:
    root = "govern"

    if word == "govern":
        suffix = "-"
        level = "Base"
    elif word == "government":
        suffix = "ment"
        level = "Level 1"
    else:
        suffix = "ance"
        level = "Level 1"

    print("\nWord:", word)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Derivation:", level)
    print("Normalized:", root)