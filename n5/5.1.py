user1_info = []
user2_info = []
user3_info = []

user1_info.append(input("Enter user 1 name: "))
user1_info.append(input("Enter user 1 surname: "))
user1_info.append(input("Enter user 1 age: "))

user2_info.append(input("Enter user 2 name: "))
user2_info.append(input("Enter user 2 surname: "))
user2_info.append(input("Enter user 2 age: "))

user3_info.append(input("Enter user 3 name: "))
user3_info.append(input("Enter user 3 surname: "))
user3_info.append(input("Enter user 3 age: "))

consumer_info = [user1_info, user2_info, user3_info]

user_index = int(input("Enter user index (1, 2, or 3): ")) - 1

if 0 <= user_index < len(consumer_info):
    print("Name:", consumer_info[user_index][0])
    print("Lastname:", consumer_info[user_index][1])
    print("Age:", consumer_info[user_index][2])
else:
    print("Invalid user index.")
