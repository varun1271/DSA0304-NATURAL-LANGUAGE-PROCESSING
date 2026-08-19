# Semantic Representation

queries = {
    "Activate international roaming": ("ACTIVATE", "Roaming"),
    "Deactivate caller tune": ("DEACTIVATE", "CallerTune"),
    "Check data balance": ("QUERY", "DataBalance"),
    "Enable 5G service": ("ACTIVATE", "5GService")
}

for query, meaning in queries.items():
    print(query, "->", meaning)

# Check prediction
actual = "DEACTIVATE"
predicted = "ACTIVATE"

print("\nActual Intent:", actual)
print("Predicted Intent:", predicted)

if actual != predicted:
    print("Error: Wrong semantic interpretation")