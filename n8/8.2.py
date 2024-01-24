length_after_filter = lambda input_list: len(list(filter(lambda name: name[0].isupper(), input_list)))

name_list_str = input("Enter a list of names separated by spaces: ")
name_list = name_list_str.split()

result_length = length_after_filter(name_list)

print(f"Original List: {name_list}")
print(f"Length after removing names starting with a lowercase letter: {result_length}")
