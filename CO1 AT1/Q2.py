import re

products = [
    "Laptop",
    "Laptop Bag",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Smart Phone",
    "Phone Charger",
    "Wireless Keyboard",
    "USB Cable"
]

keyword = input("Enter search keyword: ")

print("\nExact Match")
for p in products:
    if re.fullmatch(keyword, p, re.IGNORECASE):
        print(p)

print("\nPrefix Match")
for p in products:
    if re.match(keyword, p, re.IGNORECASE):
        print(p)

print("\nSuffix Match")
for p in products:
    if re.search(keyword + r"$", p, re.IGNORECASE):
        print(p)

print("\nPartial Match")
count = 0
for p in products:
    if re.search(keyword, p, re.IGNORECASE):
        print(p)
        count += 1

print("\nCase-Insensitive Match")
for p in products:
    if re.search(keyword, p, re.IGNORECASE):
        print(p)

print("\nReport")
print("Total Matching Products =", count)