def weight_on_moon(weight_on_earth):
    moon_gravity_ratio = 1 / 6
    weight_on_moon = weight_on_earth * moon_gravity_ratio
    return weight_on_moon

user_weight_earth = float(input("Enter your weight on Earth (in kilograms): "))

user_weight_moon = weight_on_moon(user_weight_earth)

print(f"Your weight on the Moon would be: {user_weight_moon} Kg")
