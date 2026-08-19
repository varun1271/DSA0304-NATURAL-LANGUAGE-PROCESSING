# Feature structure

subject = {
    "word": "student",
    "number": "singular"
}

verb = {
    "word": "reads",
    "number": "singular"
}

print("Feature Structure:")
print(subject)
print(verb)

if subject["number"] == verb["number"]:
    print("Subject-Verb Agreement: Correct")
else:
    print("Subject-Verb Agreement: Incorrect")


# Subcategorization

print("\nSubcategorization:")
print("give -> Subject + Verb + Recipient + Object")
print("The teacher gave the student a book.")

print("Subject: teacher")
print("Verb: gave")
print("Recipient: student")
print("Object: book")