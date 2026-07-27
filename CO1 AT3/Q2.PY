# Simple DFA Simulator

while True:
    s = input("Enter a string (or type exit): ")

    if s == "exit":
        break

    state = "q0"

    for ch in s:
        if state == "q0":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == "a":
                state = "q1"
            else:
                state = "q2"

        elif state == "q2":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

    if state == "q2":
        print("Accepted")
    else:
        print("Rejected")