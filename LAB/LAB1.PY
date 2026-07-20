import re

text = "My phone number is 9876543210"

pattern = r"\d{10}"   # Matches a 10-digit number

match = re.search(pattern, text)

if match:
    print("Phone Number Found:", match.group())
else:
    print("Phone Number Not Found")