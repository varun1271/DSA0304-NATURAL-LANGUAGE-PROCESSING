import re

text = "Meeting on 12/09/2026\nCall 9876543210\n#NLP\n@OpenAI\nnatural language processing"

while True:
    print("\n1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = re.findall(r"\d{2}/\d{2}/\d{4}", text)
        print(result)

    elif choice == "2":
        result = re.findall(r"\d{10}", text)
        print(result)

    elif choice == "3":
        result = re.findall(r"#\w+", text)
        print(result)

    elif choice == "4":
        result = re.findall(r"@\w+", text)
        print(result)

    elif choice == "5":
        p = input("Enter prefix: ")
        result = re.findall(r"\b" + p + r"\w*", text)
        print(result)

    elif choice == "6":
        s = input("Enter suffix: ")
        result = re.findall(r"\b\w*" + s + r"\b", text)
        print(result)

    elif choice == "7":
        break

    else:
        print("Invalid Choice")