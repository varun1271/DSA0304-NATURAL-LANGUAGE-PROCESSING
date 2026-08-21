# Generate a Parse Tree for a Sentence using Context-Free Grammar

import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'ball' | 'park'
    V -> 'chases' | 'sees' | 'runs'
    P -> 'in' | 'with'
""")

parser = ChartParser(grammar)

sentence = input("Enter a sentence: ")
tokens = sentence.split()

print("\nParse Trees:")
trees = list(parser.parse(tokens))

if trees:
    for tree in trees:
        tree.pretty_print()
else:
    print("No parse tree found. Sentence is invalid.")