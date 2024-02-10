######## lists
# a = []
# print(type(a))

# a = [1, 2, 3, 4, "hi", [1, 2, 3]]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[5][0])
# print(a[5][1])
# print(a[5][2])
# for symbol in a:
#     print(symbol)

first_list = [1, 2, 3, 4, "hi", [1, 2, 3]]

# first_list.clear()
# print(first_list) #clears the list

# first_list.pop()
# first_list.pop(3)
# print(first_list) #deletes last or what i have given to it
# print(first_list.pop(4)) #it can also return deleted value

# first_list.append("end")
# print(first_list) #adds value at the end

# first_list.remove(3)
# print(first_list) #deletes the element, not the index numerically. if we give it non existing index, it'll error

# first_list.reverse()
# print(first_list)



second_list = [51, 64, 61, 32, 92]

# second_list.sort()
# print(second_list)

# second_list.sort(reverse=True)
# print(second_list)

# first_list.insert(2, "inserted")
# print(first_list) #inserts value at the given index

# print(first_list.count(2)) #counts how many times the value appears

# first_list.extend([9, 5, 3, 1, 7])
# print(first_list)

# print(first_list.index(3)) #returns first index number it finds

third_list = first_list
# first_list.append(900)
# print(first_list)
# print(third_list) #both lists are the same, we may loose something

# third_list = first_list.copy()
# first_list.append(900)
# print(first_list)
# print(third_list) #second list is copy and values are saved separately

# a = [1, 2, 3]
# a[1] = 4
# print(a)

# a = [1, 2, [3, 4]]
# a[2][1] = 9
# print(a)

# first_list.append(4)
# first_list[5][2] = 17
# print(first_list)
# print(third_list) #we can change both lists by .copy but we need deepcopy

# import copy
# fourth_list = copy.deepcopy(first_list)
# first_list.append(4)
# first_list[5][2] = 17
# print(first_list)
# print(fourth_list)


# data = []
# while len(data) <5:
#     answer = input("Enter Data: ")
#     data.append(answer)
# print(data)

# x = data[0]
# data[0] = data[-1]
# data[-1] = x
# print(data)


# data = [1, 2, 3, 4]
# i = 0
# for el in data:
#     i += 1
# print(i)


# data = ["zero", "one", "two", "three", "four"]
# for index, element in enumerate(data):
#     print(index, element)


# data = ["zero", "one", "two", "three", "four"]
# print(data * 2)
# print(data[2:])

# data = input("Enter text: ").split()
# specific_list = []
# for word in data:
#     if word[0].lower() == "a":
#         specific_list.append(word)  
# print(specific_list)

# data = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# answer = input("Word: ").lower()
# if answer in data:
#     print(data.index(answer))

# data = [22, 12, -196, 2000, 53]
# # print(min(data))
# # print(max(data))
# data.sort()
# print(data[0])
# data.sort(reverse=True)
# print(data[0])

# data = [22, "hi", 54, [6, 7, 8, [8, 9, "nice"]], "lol"]
# data[3][3][2] = "catch"
# print(data)

# data = [[9, 9, 9], [6, 7, 8, [8, 9, "nice"]], ["a", "b", "c"]]
# for i in data:
#     for j in i:
#         print(j)

