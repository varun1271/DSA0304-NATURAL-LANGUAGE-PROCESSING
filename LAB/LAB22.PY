text = "Ravi went to the market. He bought some fruits. He returned home."

sentences = text.split(".")

last_person = ""

print("Text:", text)
print("\nReference Resolution:\n")

for sentence in sentences:
    words = sentence.strip().split()

    for word in words:
        word = word.strip(".,!?")

        # Identify a possible person's name
        if word and word[0].isupper() and word not in ["He", "She", "It", "They"]:
            last_person = word

        # Resolve pronouns
        if word in ["He", "She"]:
            print(word, "refers to", last_person)