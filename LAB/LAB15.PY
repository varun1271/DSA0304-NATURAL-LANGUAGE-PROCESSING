# Probabilistic Context-Free Grammar (PCFG) Parsing

import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

pcfg = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V NP [0.7] | V NP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.3] | 'cat' [0.3] | 'ball' [0.2] | 'park' [0.2]
    V -> 'chases' [0.4] | 'sees' [0.4] | 'runs' [0.2]
    P -> 'in' [0.5] | 'with' [0.5]
""")

parser = ViterbiParser(pcfg)

sentence = input("Enter a sentence: ")
tokens = sentence.split()

print("\nMost Probable Parse Tree(s):")
trees = list(parser.parse(tokens))

if trees:
    for tree in trees:
        print(tree)
        print("Probability:", tree.prob())
else:
    print("No parse tree found. Sentence is invalid.")