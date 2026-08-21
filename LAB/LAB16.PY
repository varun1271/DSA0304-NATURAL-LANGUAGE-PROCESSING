import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk is the CEO of Tesla and SpaceX. He was born in South Africa."

doc = nlp(text)

print("Named Entities:")

for entity in doc.ents:
    print("Entity:", entity.text)
    print("Label:", entity.label_)
    print("Explanation:", spacy.explain(entity.label_))
    print()