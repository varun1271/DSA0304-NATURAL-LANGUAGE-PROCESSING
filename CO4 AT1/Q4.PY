# Simple semantic role assignment

sentences = {
    "Doctor prescribed medicine to patient":
        [("Doctor", "Agent"),
         ("medicine", "Theme"),
         ("patient", "Recipient")],

    "Patient reported severe headache":
        [("Patient", "Agent"),
         ("headache", "Symptom")],

    "Nurse monitored patient continuously":
        [("Nurse", "Agent"),
         ("patient", "Object")],

    "Medicine reduced blood pressure":
        [("Medicine", "Agent"),
         ("blood pressure", "Affected")]

}

for sentence, roles in sentences.items():

    print("\nSentence:", sentence)

    for word, role in roles:
        print(word, "->", role)