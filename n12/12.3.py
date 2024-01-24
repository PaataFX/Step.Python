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
