# Morphological Parsing Module

words = ["unhappy", "happiness", "happily"]

for word in words:

    prefix = "-"
    suffix = "-"
    base = ""
    kind = "Derivational"

    if word.startswith("un"):
        prefix = "un"
        base = "happy"

    elif word.endswith("ness"):
        suffix = "ness"
        base = "happy"

    elif word.endswith("ly"):
        suffix = "ly"
        base = "happy"

    print("-" * 50)
    print("Word :", word)
    print("Prefix :", prefix)
    print("Base :", base)
    print("Suffix :", suffix)
    print("Type :", kind)
    print("Normalized :", "happy")