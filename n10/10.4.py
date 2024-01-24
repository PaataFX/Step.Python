import random
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time, result
    return wrapper

@timing_decorator
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

@timing_decorator
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def generate_random_integers(length, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(length)]

list_lengths = [10000, 100000, 1000000]

for length in list_lengths:
    random_numbers = generate_random_integers(length, 1, length)

    sorted_random_numbers = sorted(random_numbers)

    linear_time, linear_search_result = linear_search(sorted_random_numbers, random.choice(sorted_random_numbers))

    binary_time, binary_search_result = binary_search(sorted_random_numbers, random.choice(sorted_random_numbers))

    print(f"\nFor a list of length {length}:")
    print(f"Linear Search took {linear_time:.6f} seconds")
    print(f"Binary Search took {binary_time:.6f} seconds")

    if linear_time < binary_time:
        print("Linear Search was faster.")
    elif linear_time > binary_time:
        print("Binary Search was faster.")
    else:
        print("Both search methods took the same time.")
