words = ["analyzing", "analysis", "analytical"]

for word in words:
    root = "analyze"

    if word == "analyzing":
        suffix = "ing"
        form = "Inflectional"
    elif word == "analysis":
        suffix = "sis"
        form = "Derivational"
    else:
        suffix = "ical"
        form = "Derivational"

    print("\nWord:", word)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Type:", form)
    print("Normalized:", root)