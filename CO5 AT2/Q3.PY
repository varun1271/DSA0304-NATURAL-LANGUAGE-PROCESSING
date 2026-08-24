def identify_dialogue_act(utterance):
    utterance = utterance.lower()

    if "can you" in utterance:
        return "Request"

    elif "where" in utterance or "?" in utterance:
        return "Question"

    elif "i want" in utterance:
        return "Inform"

    elif "has been booked" in utterance:
        return "Action / Confirmation"

    else:
        return "Unknown"


conversation = [
    "Can you book a train ticket for me?",
    "Sure, where would you like to travel?",
    "I want to go to Chennai.",
    "Your ticket has been booked."
]

print("Dialogue Act Sequence:")

for sentence in conversation:
    act = identify_dialogue_act(sentence)
    print(f"{sentence} --> {act}")