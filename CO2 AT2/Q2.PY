words = ["disagree", "agreement", "agreeable"]

for word in words:
    prefix = ""
    suffix = ""
    root = "agree"

    if word == "disagree":
        prefix = "dis"
        meaning = "Negative"
    elif word == "agreement":
        suffix = "ment"
        meaning = "State of agreeing"
    else:
        suffix = "able"
        meaning = "Capable of agreeing"

    print("\nWord:", word)
    print("Prefix:", prefix)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Meaning:", meaning)
    print("Normalized:", root)