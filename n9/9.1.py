import random

random_list = [random.randint(1, 100) for _ in range(10)]

print("Original List:", random_list)

random_list.sort()

print("Sorted List:", random_list)