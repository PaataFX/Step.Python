import random

def generate_random_integers(length, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(length)]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sort_random_integers(random_numbers, choice):
    if choice == 1:
        sorted_numbers = bubble_sort(random_numbers.copy())
    elif choice == 2:
        sorted_numbers = quick_sort(random_numbers.copy())
    elif choice == 3:
        sorted_numbers = sorted(random_numbers)
    else:
        print("Invalid choice. Using Python's built-in sorted.")
        sorted_numbers = sorted(random_numbers)
    return sorted_numbers

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

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

length = int(input("Enter the length of the list: "))
minimum = int(input("Enter the minimum value: "))
maximum = int(input("Enter the maximum value: "))

random_numbers = generate_random_integers(length, minimum, maximum)

print("\nSelect a sorting algorithm:")
print("1. Bubble Sort")
print("2. QuickSort")
print("3. Python's built-in sorted")

choice = int(input("Enter your choice (1, 2, or 3): "))

sorted_random_numbers = sort_random_integers(random_numbers, choice)

print("\nSorted List:", sorted_random_numbers)

element_to_find = int(input("\nEnter the element to find: "))

linear_result = linear_search(sorted_random_numbers, element_to_find)
print(f"Linear Search: Element {element_to_find} {'found at index ' + str(linear_result) if linear_result != -1 else 'not found'}")

binary_result = binary_search(sorted_random_numbers, element_to_find)
print(f"Binary Search: Element {element_to_find} {'found at index ' + str(binary_result) if binary_result != -1 else 'not found'}")
