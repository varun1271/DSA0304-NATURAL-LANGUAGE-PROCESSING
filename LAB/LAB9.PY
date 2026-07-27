import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),   # Verb ending with ing
    (r'.*ed$', 'VBD'),    # Verb ending with ed
    (r'.*ly$', 'RB'),     # Adverb
    (r'.*s$', 'NNS'),     # Plural noun
    (r'.*', 'NN')         # Default noun
]

tagger = RegexpTagger(patterns)

text = input("Enter a sentence: ")
words = word_tokenize(text)

print(tagger.tag(words))