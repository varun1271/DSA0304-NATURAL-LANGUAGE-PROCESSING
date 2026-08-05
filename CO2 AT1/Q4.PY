# Finite-State Morphological Parser

words = ["writes", "writing", "written"]

for word in words:

    if word == "writes":
        states = "Start -> Root(write) -> +s -> End"
        root = "write"
        pattern = "Regular"

    elif word == "writing":
        states = "Start -> Root(write) -> +ing -> End"
        root = "write"
        pattern = "Regular"

    elif word == "written":
        states = "Start -> Root(write) -> Irregular Form -> End"
        root = "write"
        pattern = "Irregular"

    print("-" * 60)
    print("Word :", word)
    print("State Transition :", states)
    print("Root :", root)
    print("Pattern :", pattern)
    print("Normalized :", root)