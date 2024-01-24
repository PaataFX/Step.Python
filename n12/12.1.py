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
