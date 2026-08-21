# Earley Parser for Context-Free Grammar

# Grammar rules:
# S  -> NP VP
# NP -> Det N | Det N PP
# VP -> V NP | V NP PP
# PP -> P NP
# Det -> "the" | "a"
# N  -> "dog" | "cat" | "ball" | "park"
# V  -> "chases" | "sees" | "runs"
# P  -> "in" | "with"

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["Det", "N", "PP"]],
    "VP": [["V", "NP"], ["V", "NP", "PP"]],
    "PP": [["P", "NP"]],
    "Det": ["the", "a"],
    "N": ["dog", "cat", "ball", "park"],
    "V": ["chases", "sees", "runs"],
    "P": ["in", "with"],
}

def is_terminal(sym):
    return sym not in grammar

def get_rules(sym):
    return grammar.get(sym, [])

# State: (rule_left, rule_right, dot_position, start_index)
def earley_parse(tokens):
    n = len(tokens)
    charts = [[] for _ in range(n + 1)]

    # Start state
    charts[0].append(("GAMMA", ["S"], 0, 0))

    for i in range(n + 1):
        j = 0
        while j < len(charts[i]):
            state = charts[i][j]
            left, right, dot, start = state
            j += 1

            # Completed
            if dot >= len(right):
                complete(charts, state, i)
            else:
                sym = right[dot]
                if is_terminal(sym):
                    scan(charts, state, i, tokens)
                else:
                    predict(charts, sym, i)

    # Check if GAMMA -> S . was completed at end
    for state in charts[n]:
        if state[0] == "GAMMA" and state[2] >= len(state[1]) and state[3] == 0:
            return True
    return False

def predict(charts, sym, i):
    for rule in get_rules(sym):
        # Wrap string terminals as single-element lists
        if isinstance(rule, str):
            rule = [rule]
        state = (sym, rule, 0, i)
        if state not in charts[i]:
            charts[i].append(state)

def scan(charts, state, i, tokens):
    left, right, dot, start = state
    sym = right[dot]
    if i < len(tokens) and tokens[i] == sym:
        new_state = (left, right, dot + 1, start)
        if new_state not in charts[i + 1]:
            charts[i + 1].append(new_state)

def complete(charts, state, i):
    left, right, dot, start = state
    for s in charts[start]:
        s_left, s_right, s_dot, s_start = s
        if s_dot < len(s_right) and s_right[s_dot] == left:
            new_state = (s_left, s_right, s_dot + 1, s_start)
            if new_state not in charts[i]:
                charts[i].append(new_state)

sentence = input("Enter a sentence: ")
tokens = sentence.split()

if earley_parse(tokens):
    print("Sentence is Valid (Parsed Successfully)")
else:
    print("Sentence is Invalid (Parse Failed)")