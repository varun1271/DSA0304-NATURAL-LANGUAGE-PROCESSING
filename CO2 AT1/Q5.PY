from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

for word in words:

    print("-" * 50)
    print("Original Word :", word)

    step1 = word

    if word.endswith("al"):
        step2 = word[:-2]
        rule = "Removed 'al'"
    elif word.endswith("ion"):
        step2 = word[:-3]
        rule = "Removed 'ion'"
    elif word.endswith("ate"):
        step2 = word[:-3]
        rule = "Removed 'ate'"
    else:
        step2 = word
        rule = "No Rule"

    final_stem = ps.stem(word)

    print("Rule Applied :", rule)
    print("Intermediate :", step2)
    print("Final Stem :", final_stem)