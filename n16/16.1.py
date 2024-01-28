# წრის კლასი, რომელსაც აქვს მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.
class Circle:
    radius = int(input("please, enter a radius of a circle: "))
    @classmethod
    def perimeter(cls):
        perimeter = 2*cls.radius*3.14
        print(f"The Perimeter of The circle is {perimeter}")
    @classmethod
    def area(cls):
        area = (cls.radius**2)*3.14
        print(f"The Area of The circle is {area}")

Circle.perimeter()
Circle.area()

