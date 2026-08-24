def parser(word):

    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse"
    }

    if word in irregular:
        return irregular[word], "Plural"

    if word.endswith("ies"):
        return word[:-3] + "y", "Plural"

    if word.endswith("es"):
        return word[:-2], "Plural"

    if word.endswith("s"):
        return word[:-1], "Plural"

    return word, "Singular"

words = ["cars", "boxes", "cities", "children",
         "men", "books"]

for w in words:
    print(w, "->", parser(w))
