import random

def generate_random_integers(length, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(length)]