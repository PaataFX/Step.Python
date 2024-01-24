#ლექსიკონი რომელიც დუბლიკატებს არ იღებს
def remove_duplicates(input_dict):
    seen_values = set()
    unique_dict = {}

    for key, value in input_dict.items():
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)

    return unique_dict

input_dict = dict(input("Enter a dictionary (in the format {key1: value1, key2: value2, ...}): "))
result = remove_duplicates(input_dict)
print(result)

# სიცარიელის შემოწმება
def check_empty(dictionary):
    if not dictionary:
        return "Dictionary is empty"
    else:
        return "Dictionary is not empty"

input_dict = dict(input("Enter a dictionary (in the format {key1: value1, key2: value2, ...}): "))
result = check_empty(input_dict)
print(result)

# ლექსიკონდა გვაძლევს შეყვანილი ინფორმაციის წევრების რაოდენობებს
def create_dictionary(input_string, key_place=0):
    char_count = {}

    for char in input_string:
        key = char[key_place]

        if key in char_count:
            char_count[key] += 1
        else:
            char_count[key] = 1

    return char_count

input_str = input("Enter a string: ")
result = create_dictionary(input_str)
print(result)
