def recognize_dialog_act(sentence):

    sentence = sentence.lower().strip()

    if any(word in sentence for word in ["hello", "hi", "hey"]):
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif any(word in sentence for word in ["please", "can you", "could you"]):
        return "Request"

    elif any(word in sentence for word in ["bye", "goodbye", "see you"]):
        return "Farewell"

    else:
        return "Statement"


sentence = input("Enter a sentence: ")

result = recognize_dialog_act(sentence)

print("Dialog Act:", result)