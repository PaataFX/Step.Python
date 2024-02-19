# from random import randint
# def list_generator(n, k):
#     arr = []
#     for _ in range(1, k):
#         arr.append(randint(1, k))
#     return arr

# new_list = list_generator(10, 100)
# print(new_list)

# # new_list.sort()
# # print(new_list)

# b = sorted(new_list, reverse=True)
# print(b)

# new_list2 = [["Elena", 21, 90], ["Maria", 18, 86], ["David", 24, 89]]
# # new_list2.sort()
# new_list2.sort(key=lambda a: a[1])
# print(new_list2)



from random import randint
def list_generator(n, k):
    arr = []
    for _ in range(1, k):
        arr.append(randint(1, k))
    return arr
new_list = list_generator(20, 1000)


# def bubble(list_a):
#     indexing_length = len(list_a) - 1
#     sorteed = False
    
#     while not sorteed:
#         sorteed = True
        
#         for i in range(0, indexing_length):
#             if list_a[i] > list_a[i+1]:
#                 sorteed = False
#                 list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
#     return list_a
# print(new_list)
# print(bubble(new_list))


# def selection_sort(some_arr):
#     arr = some_arr
#     indexing_length = range(0, len(arr)-1)
    
#     for i in indexing_length:
#         min_value = 1
        
#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_value]:
#                 min_value = j

#         if min_value != i:
#             arr[min_value], arr[i] = arr[i], arr[min_value]
    
#     print("selection sort")
#     return arr
# print(selection_sort(new_list))


# def insertion_sort(some_arr):
#     arr = some_arr
#     indexing_length = range(1, len(arr))
    
#     for i in indexing_length:
#         value_to_sort = arr[i]
        
#         while arr [i-1] > value_to_sort and i > 0:
#             arr[i], arr[i-1] = arr[i-1], arr[i]
#             i = i - 1
            
#     print("insertion sort")
    
# print(new_list)
# print(insertion_sort(new_list))


# def quick_sort(some_arr):
#     arr = some_arr
#     length = len(arr)
#     if length <=1:
#         return arr
#     else:
#         pivot = arr.pop()
    
#     items_greater=[]
#     items_lower = []
    
#     for item in arr:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
        
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# print("quick sort")
# print(new_list)
# print(quick_sort(new_list))


