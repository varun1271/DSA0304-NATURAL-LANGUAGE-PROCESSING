def analyze_discourse(sentences):
    relations = []

    for i in range(len(sentences) - 1):
        current = sentences[i]
        next_sentence = sentences[i + 1]

        if "Therefore" in next_sentence:
            relation = "Cause-Effect"
        elif i == 1:
            relation = "Sequence / Consequence"
        else:
            relation = "Elaboration"

        relations.append(
            f"Sentence {i + 1} -> Sentence {i + 2}: {relation}"
        )

    return relations


sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

result = analyze_discourse(sentences)

print("Discourse Relations:")
for relation in result:
    print(relation)