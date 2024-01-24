# მომხმარებელთა ბაზა


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


# რეგისტრაცია 


registered_users = []
name = input("Enter your username: ")
password = input("Enter your password (at least 8 characters): ")

if name and len(password) >= 8:
    registered_users.append([name, password])
    print("Registration successful!")
else:
    print("Registration failed. Username should not be empty, and the password should be at least 8 characters.")

login_name = input("Enter your username ")
login_password = input("Enter your password: ")

login_successful = any(user[0] == login_name and user[1] == login_password for user in registered_users)

if login_successful:
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")



# მსახიობების სია


actors_list = [
    {"first_name": "Leonardo", "last_name": "DiCaprio", "age": 47, "movies": ["Titanic", "Inception", "The Revenant"]},
    {"first_name": "Brad", "last_name": "Pitt", "age": 58, "movies": ["Fight Club", "Inglourious Basterds", "Se7en"]},
    {"first_name": "Meryl", "last_name": "Streep", "age": 72, "movies": ["The Devil Wears Prada", "Mamma Mia!", "Sophie's Choice"]},
    {"first_name": "Denzel", "last_name": "Washington", "age": 66, "movies": ["Training Day", "Malcolm X", "Flight"]},
    {"first_name": "Scarlett", "last_name": "Johansson", "age": 37, "movies": ["Lost in Translation", "The Avengers", "Marriage Story"]},
    {"first_name": "Tom", "last_name": "Hanks", "age": 66, "movies": ["Forrest Gump", "Cast Away", "Saving Private Ryan"]}
]

while True:
    actor_name = input("Enter the actor's first or last name (or 'exit' to quit): ")

    if actor_name.lower() == 'exit':
        break

    found_actor = None
    for actor in actors_list:
        if actor_name.lower() in (actor["first_name"].lower(), actor["last_name"].lower()):
            found_actor = actor
            break

    if found_actor:
        print("Actor Summary:")
        print("Name:", found_actor["first_name"], found_actor["last_name"])
        print("Age:", found_actor["age"])
        print("Movies:", ", ".join(found_actor["movies"]))
    else:
        print("Actor not found in the list. Try again.")
