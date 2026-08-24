def reference_resolution(text):
    entities = {
        "Ravi": "male",
        "Arun": "male",
        "book": "object"
    }

    # Pronoun resolution based on discourse context
    resolved_text = text.replace("He", "Ravi")
    resolved_text = resolved_text.replace("it", "the book")

    return resolved_text


text = "Ravi met Arun at the library. He borrowed a book and later returned it."

result = reference_resolution(text)

print("Original:", text)
print("Resolved:", result)