# Search queries and clicked results

data = {
    "Apple accessories": "iPhone Charger",
    "Mouse wireless": "Bluetooth Mouse",
    "Java tutorial": "Coding Lessons",
    "Python course": "Software Development Training"
}

for query, result in data.items():

    if "Apple" in query:
        sense = "Technology Brand"

    elif "Mouse" in query:
        sense = "Computer Device"

    elif "Java" in query:
        sense = "Programming Language"

    elif "Python" in query:
        sense = "Programming Language"

    print("\nQuery:", query)
    print("Clicked Result:", result)
    print("Correct Sense:", sense)