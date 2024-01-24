sum_positive_negative = lambda input_list: (
    sum(filter(lambda x: x > 0, input_list)),
    sum(filter(lambda x: x < 0, input_list))
)

num_list_str = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(float, num_list_str.split()))

positive_sum, negative_sum = sum_positive_negative(num_list)

print(f"Original List: {num_list}")
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
