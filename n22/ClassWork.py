import json

# # json_data = '{"name": "george", "car": true}'
# print(json.loads(json_data))
# print(json.dumps(json_data))



# with open("new.json", "r") as file:
#     python_data = json.load(file)
    
# python_data["key"].append("New Item")

# with open("new.json", "w") as file:
#     python_data = json.dump(python_data, file)



# class SomeClass:
#     def __init__(self, name, lastname, age, car):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.car = car

# human = SomeClass("Lado", "Khimshishvili", 24, True)

# json_data = json.dumps(human.__dict__)
# print(SomeClass(**json.loads(json_data)))


# class SomeClass:
#     def __init__(self, name, lastname, age, car):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.car = car

#     def __repr__(self):
#         return f"{self.name} {self.lastname}"

# human = SomeClass("Lado", "Khimshishvili", 24, True)

# import pickle

# a = "Ordinary string..."
# data = pickle.dumps(human)
# print(data)
# print(pickle.loads(data))



# class SomeClass:
#     def __init__(self, name, lastname, age, car):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.car = car

#     def __repr__(self):
#         return f"{self.name} {self.lastname}"

# human = SomeClass("Lado", "Khimshishvili", 24, True)

import pickle

# with open("can_of.pickle", "wb") as file:
#     pickle.dump(human, file)

# with open("can_of.pickle", "rb") as file:
#     print(pickle.load(file))

import dill

# with open("can_of_dill.pickle", "wb") as file:
#     dill.dump(human, file)

# with open("can_of_dill.pickle", "rb") as file:
#     print(dill.load(file))




# class SomeClass:
#     def __init__(self, name, lastname, age, car):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.car = car

#     def __repr__(self):
#         return f"{self.name} {self.lastname}"

# a = {"first": 1, "second": 2}
# b = SomeClass("Lado", "Khimshishvili", 24, True)
# c = lambda x: x**2

# object_list = [a, b, c]

# def serialize_now(obj):
#     # 1) ჯერ ცადოს სერიალიზაცია json ფორმატში
#     try:
#         with open("data.json", "a") as file:
#             json.dump(obj, file)
#         print('Json Format')

#     # 2) თუ არ გამოვიდა ცადოს სერიალიზაცია pickle ფორმატში
#     except:
#         try:
#             with open("data.pickle", "ab") as file:
#                 pickle.dump(obj, file)
#             print('Pickle Format')
#     # 3) თუ არ გამოვიდა ცადოს სერიალიზაცია dill ფორმატში
#         except:
#             try:
#                 with open("data_dill.pkl", "ab") as file:
#                     dill.dump(obj, file)
#                 print('Dill Format')
#             except:
#                 print("Object is not Serializable!")

# for obj in object_list:
#     serialize_now(obj)



import pickle

#1 მეგობრის კლასი

all_questions = [
    "Name your favorite Movie",
    "Name your favorite Sport",
    "What is your hobby",
    "Can you swim"
]

class Friend:
    def __init__(self, name, lastname, questions):
        self.name = name
        self.lastname = lastname
        self.questions = questions
        self.result = {}

    def interview(self):
        print("Interview has started!")
        for question in self.questions:
            answer = input(f"{question}?")
            self.result[question] = answer


    def __repr__(self):
        print(f"{self.name} {self.lastname}")
        for key, value in self.result.items():
            print(key, "___", value)
        return f"{self.name} {self.lastname}"


while True:
    answer = input("Quit/Record interview/Read result (0/1/2): ")
    if answer == "0":
        break

    if answer == "1":
        name = input("Enter your name: ")
        lastname = input("Enter your lastname: ")

        new_friend = Friend(name, lastname, all_questions)

        new_friend.interview()

        with open(f"{name}_{lastname}.pickle", "wb") as file:
            pickle.dump(new_friend, file)

    elif answer == "2":
        name = input("Enter respondent name: ")
        lastname = input("Enter respondent lastname: ")

        try:
            with open(f"{name}_{lastname}.pickle", "rb") as file:
                print(pickle.load(file))

        except:
            print("Respondent not found!")