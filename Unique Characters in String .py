text = input("Enter a string: ")
text = text.replace(" ", "").lower()
unique_chars = set()

for char in text:
    if char in unique_chars:
        print(False)
        break
    unique_chars.add(char)
else:
    print(True)