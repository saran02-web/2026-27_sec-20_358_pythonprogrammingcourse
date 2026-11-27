s = input("Enter the string: ")

vowels = consonants = digits = spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch.isspace():
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
