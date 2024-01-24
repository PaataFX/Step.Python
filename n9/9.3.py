import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_sorting_time(sorting_function, data_size):
    random_list = generate_random_list(data_size)
    start_time = time.time()
    sorting_function(random_list)
    end_time = time.time()
    return end_time - start_time

def main():
    data_sizes = [1000, 2000, 3000]

    for size in data_sizes:
        print(f"\nData Size: {size} items")

        bubble_sort_time = measure_sorting_time(bubble_sort, size)
        print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")

        selection_sort_time = measure_sorting_time(selection_sort, size)
        print(f"Selection Sort Time: {selection_sort_time:.6f} seconds")

if __name__ == "__main__":
    main()
