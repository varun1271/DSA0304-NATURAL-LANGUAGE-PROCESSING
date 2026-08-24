import re
def parser(word):
    prefixes = ["un", "re"]
    suffixes = ["ing", "able", "est", "s"]
    prefix = ""
    suffix = ""
    for p in prefixes:
        if word.startswith(p):
            prefix = p
            word = word[len(p):]
            break
    for s in suffixes:
        if word.endswith(s):
            suffix = s
            word = word[:-len(s)]
            break
    return prefix, word, suffix
words = ["happiest", "unbelievable", "running",
         "reordering", "smartphones", "unreadable"]
for w in words:
    print(w, "->", parser(w))

