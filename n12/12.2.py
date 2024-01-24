def check_empty(dictionary):
    if not dictionary:
        return "Dictionary is empty"
    else:
        return "Dictionary is not empty"

input_dict = dict(input("Enter a dictionary (in the format {key1: value1, key2: value2, ...}): "))
result = check_empty(input_dict)
print(result)
