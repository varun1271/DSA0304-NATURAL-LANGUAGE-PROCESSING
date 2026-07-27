tags = {
    "Ram": "NNP",
    "is": "VBZ",
    "playing": "VBG",
    "cricket": "NN"
}

sentence = input("Enter a sentence: ")

for word in sentence.split():
    print(word, ":", tags.get(word, "Unknown"))