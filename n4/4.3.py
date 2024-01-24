sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

if all(char in sentence2 for char in sentence1) and all(char in sentence1 for char in sentence2):
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")
