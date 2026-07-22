word = input("Enter a noun: ")

if word.endswith(("s", "x", "z", "ch", "sh")):
    plural = word + "es"
else:
    plural = word + "s"

print("Plural Form:", plural)