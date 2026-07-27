import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize

text = input("Enter a sentence: ")

words = word_tokenize(text)
tagged = nltk.pos_tag(words)

print("POS Tags:")
for word, tag in tagged:
    print(word, ":", tag)