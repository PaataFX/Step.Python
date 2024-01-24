sentence = input("Enter a sentence: ")

num_letters = 0
num_numbers = 0
num_symbols = 0

for char in sentence:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_numbers += 1
    else:
        num_symbols += 1

print("Number of letters:", num_letters)
print("Number of numbers:", num_numbers)
print("Number of symbols:", num_symbols)
