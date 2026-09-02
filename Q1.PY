# Simple Word Sense Disambiguation for the word "bank"

finance_words = {
    "money", "deposit", "deposited", "account",
    "savings", "customer", "cash", "loan",
    "interest", "withdraw", "cheque", "atm", "branch"
}

river_words = {
    "river", "water", "stream", "shore", "sat",
    "flood", "fisherman", "boat", "fish",
    "current", "flow", "walked", "bridge"
}

def wsd(sentence):
    words = sentence.lower().replace(".", "").split()

    finance_score = 0
    river_score = 0

    for word in words:
        if word in finance_words:
            finance_score += 1
        if word in river_words:
            river_score += 1

    if finance_score > river_score:
        return "FINANCIAL"
    elif river_score > finance_score:
        return "RIVER"
    else:
        return "UNKNOWN"


# Test sentences
s1 = "The customer deposited money in the bank."
s2 = "The children sat on the bank of the river."
s3 = "The fisherman walked along the bank."

print(s1, "->", wsd(s1))
print(s2, "->", wsd(s2))
print(s3, "->", wsd(s3))