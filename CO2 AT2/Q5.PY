words = ["create", "creates", "creating"]

for word in words:
    root = "create"

    if word == "create":
        suffix = "-"
        category = "Base Form"
    elif word == "creates":
        suffix = "s"
        category = "Third Person Singular"
    else:
        suffix = "ing"
        category = "Present Participle"

    print("\nWord:", word)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Category:", category)
    print("Normalized:", root)