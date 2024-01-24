sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

result = ''.join([a + b for a, b in zip(sentence1, sentence2[::-1])])

print("Generated sentence:", result)
