import random

random_list = [random.randint(1, 100) for _ in range(10)]

print("Original List:", random_list)

sorted_list_desc = sorted(random_list, reverse=True)

print("Sorted List (Descending):", sorted_list_desc)
