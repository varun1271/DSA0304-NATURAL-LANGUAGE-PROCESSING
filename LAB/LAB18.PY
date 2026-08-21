import re

expression = input("Enter a logical expression: ")

# Pattern for Predicate(Argument)
pattern = r"([A-Za-z]+)\(([A-Za-z]+)\)"

matches = re.findall(pattern, expression)

if matches:
    print("\nPredicates found:")

    for predicate, argument in matches:
        print("Predicate:", predicate)
        print("Argument:", argument)
else:
    print("Invalid FOPC expression")