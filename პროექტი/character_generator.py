import random

class Character:
    def __init__(self, race, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.race = race
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

def generate_character(race, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
    return Character(race, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma)
