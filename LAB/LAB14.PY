# Check for Agreement in Sentences based on Context-Free Grammar Rules

# Grammar with subject-verb agreement:
# S  -> NP_SG VP_SG | NP_PL VP_PL
# NP_SG -> Det_SG N_SG
# NP_PL -> Det_PL N_PL
# VP_SG -> V_SG
# VP_PL -> V_PL
# Det_SG -> "the" | "a"
# Det_PL -> "the" | "some"
# N_SG -> "dog" | "cat" | "boy"
# N_PL -> "dogs" | "cats" | "boys"
# V_SG -> "runs" | "eats" | "sleeps"
# V_PL -> "run" | "eat" | "sleep"

grammar = {
    "S": [["NP_SG", "VP_SG"], ["NP_PL", "VP_PL"]],
    "NP_SG": [["Det_SG", "N_SG"]],
    "NP_PL": [["Det_PL", "N_PL"]],
    "VP_SG": [["V_SG"]],
    "VP_PL": [["V_PL"]],
    "Det_SG": ["the", "a"],
    "Det_PL": ["the", "some"],
    "N_SG": ["dog", "cat", "boy"],
    "N_PL": ["dogs", "cats", "boys"],
    "V_SG": ["runs", "eats", "sleeps"],
    "V_PL": ["run", "eat", "sleep"],
}

def is_terminal(sym):
    return sym not in grammar

def parse(symbol, tokens, pos):
    if is_terminal(symbol):
        if pos < len(tokens) and tokens[pos] == symbol:
            return [pos + 1]
        else:
            return []

    positions = []
    for rule in grammar[symbol]:
        if isinstance(rule, str):
            if pos < len(tokens) and tokens[pos] == rule:
                positions.append(pos + 1)
        else:
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
    print("Sentence has Valid Agreement (Grammatically Correct)")
else:
    print("Sentence has Invalid Agreement (Grammatically Incorrect)")