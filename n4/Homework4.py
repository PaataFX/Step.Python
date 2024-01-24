# თვლის მომხმარებლის შემოტანილი წინადადების ასოებს, რიცხვებსა და სიმბოლოებს
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

# კოდი, რომელიც ორ წინადადებას ერთში კრებავს
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

result = ''.join([a + b for a, b in zip(sentence1, sentence2[::-1])])

print("Generated sentence:", result)



# შემოწმება, არის თუ არა ორივე წინადადების სიმბოლოები ერთნაირი
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

if all(char in sentence2 for char in sentence1) and all(char in sentence1 for char in sentence2):
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")
