def surface_realization(action, agent, obj, tense):

    # Convert verb based on tense
    if tense.lower() == "past":
        if action.lower() == "buy":
            verb = "bought"
        else:
            verb = action + "ed"
    else:
        verb = action

    # Create sentence
    sentence = f"The {agent.lower()} {verb} a {obj.lower()}."

    return sentence


action = "Buy"
agent = "Student"
obj = "Book"
tense = "Past"

result = surface_realization(action, agent, obj, tense)

print("Generated Sentence:")
print(result)