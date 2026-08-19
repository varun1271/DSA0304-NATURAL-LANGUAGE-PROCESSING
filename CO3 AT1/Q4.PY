import random

# Lexical dictionary
dictionary = {
    "the": "DT",
    "a": "DT",
    "an": "DT",
    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "school": "NN",
    "python": "NNP",
    "is": "VBZ",
    "are": "VBP",
    "was": "VBD",
    "read": "VB",
    "reading": "VBG",
    "write": "VB",
    "writing": "VBG",
    "learn": "VB",
    "learning": "VBG",
    "quick": "JJ",
    "quickly": "RB",
    "he": "PRP",
    "she": "PRP",
    "they": "PRP",
    "in": "IN",
    "on": "IN",
    "and": "CC",
    "but": "CC"
}

# Rule-Based Tagger
def rule_based(sentence):
    words = sentence.lower().split()
    result = []

    for word in words:

        if word in dictionary:
            tag = dictionary[word]

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        result.append((word, tag))

    return result


# Simple stochastic probabilities
tag_probability = {
    "student": {"NN": 0.9, "VB": 0.1},
    "read": {"VB": 0.8, "NN": 0.2},
    "book": {"NN": 0.9, "VB": 0.1},
    "reading": {"VBG": 0.9, "NN": 0.1}
}

def stochastic(sentence):
    words = sentence.lower().split()
    result = []

    for word in words:

        if word in tag_probability:
            tag = max(
                tag_probability[word],
                key=tag_probability[word].get
            )

        elif word in dictionary:
            tag = dictionary[word]

        else:
            tag = "NN"

        result.append((word, tag))

    return result


# Transformation-Based Tagging
def transformation(sentence):
    result = rule_based(sentence)

    for i in range(1, len(result)):
        word, tag = result[i]
        previous_word, previous_tag = result[i-1]

        # Rule: after pronoun, word may be a verb
        if previous_tag == "PRP" and tag == "NN":
            result[i] = (word, "VB")

        # Rule: after auxiliary verb, word is likely a verb
        if previous_tag in ["VBZ", "VBP", "VBD"] and tag == "NN":
            result[i] = (word, "VB")

    return result


sentence = input("Enter an English sentence: ")

print("\nRule-Based Tagger:")
print(rule_based(sentence))

print("\nStochastic Tagger:")
print(stochastic(sentence))

print("\nTransformation-Based Tagger:")
print(transformation(sentence))