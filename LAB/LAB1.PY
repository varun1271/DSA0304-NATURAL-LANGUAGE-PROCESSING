import re

text = input("Enter a text: ")
pattern = input("Enter pattern to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern Found")
else:
    print("Pattern Not Found")