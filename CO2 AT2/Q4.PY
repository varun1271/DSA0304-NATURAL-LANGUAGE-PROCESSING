words = ["activate", "activation", "reactivation"]

for word in words:
    prefix = ""
    suffix = ""
    root = "activate"

    if word == "activate":
        sequence = "Base"
    elif word == "activation":
        suffix = "ion"
        sequence = "activate + ion"
    else:
        prefix = "re"
        suffix = "ion"
        sequence = "re + activate + ion"

    print("\nWord:", word)
    print("Prefix:", prefix)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Sequence:", sequence)
    print("Normalized:", root)