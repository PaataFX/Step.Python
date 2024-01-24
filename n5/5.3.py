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
