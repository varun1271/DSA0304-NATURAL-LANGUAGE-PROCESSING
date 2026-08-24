def hybrid_translation(sentence):

    # Step 1: Analyze source sentence
    source_analysis = {
        "agent": "boy",
        "action": "play",
        "object": "football",
        "tense": "present",
        "aspect": "continuous"
    }

    # Step 2: Create Interlingua representation
    interlingua = (
        f"ACTION={source_analysis['action']}, "
        f"AGENT={source_analysis['agent']}, "
        f"OBJECT={source_analysis['object']}, "
        f"TENSE={source_analysis['tense']}, "
        f"ASPECT={source_analysis['aspect']}"
    )

    # Step 3: Generate candidate Tamil translations
    candidates = [
        "சிறுவன் கால்பந்து விளையாடிக்கொண்டிருக்கிறான்.",
        "பையன் கால்பந்து விளையாடுகிறான்.",
        "சிறுவன் கால்பந்து விளையாடினான்."
    ]

    # Step 4: Statistical scores
    scores = [0.95, 0.80, 0.40]

    # Select candidate with highest score
    best_index = scores.index(max(scores))
    best_translation = candidates[best_index]

    return interlingua, candidates, scores, best_translation


sentence = "The boy is playing football."

interlingua, candidates, scores, translation = hybrid_translation(sentence)

print("Source Sentence:", sentence)
print("\nInterlingua:")
print(interlingua)

print("\nCandidate Translations:")
for candidate, score in zip(candidates, scores):
    print(candidate, "- Score:", score)

print("\nFinal Translation:")
print(translation)