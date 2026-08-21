# Simple Top-Down (Recursive Descent) Parser for Context-Free Grammar

# Grammar rules:
# S  -> NP VP
# NP -> Det N
# VP -> V NP
# Det -> "the" | "a"
# N  -> "dog" | "cat" | "ball"
# V  -> "chases" | "sees"

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": ["the", "a"],
    "N": ["dog", "cat", "ball"],
    "V": ["chases", "sees"],
}

def parse(symbol, tokens, pos):
    # If symbol is a terminal (a word)
    if symbol not in grammar:
        if pos < len(tokens) and tokens[pos] == symbol:
            return [pos + 1]
        else:
            return []

    positions = []
    for rule in grammar[symbol]:
        # rule is a list of symbols (for non-terminals) or a string (for terminals)
        if isinstance(rule, str):
            # Terminal option
            if pos < len(tokens) and tokens[pos] == rule:
                positions.append(pos + 1)
        else:
            # Non-terminal expansion
            current = [pos]
            for sym in rule:
                next_positions = []
                for c in current:
                    res = parse(sym, tokens, c)
                    next_positions.extend(res)
                current = next_positions
                if not current:
                    break
            positions.extend(current)
    return positions

sentence = input("Enter a sentence: ")
tokens = sentence.split()

result = parse("S", tokens, 0)

if result and len(tokens) in result:
    print("Sentence is Valid (Parsed Successfully)")
else:
    print("Sentence is Invalid (Parse Failed)")