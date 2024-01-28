# წრის კლასი, რომელსაც აქვს მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად, მომხმარებელმა მხოლოდ უნდა შეიყვანოს რადიუსი.
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

# კალკულატორის კლასი მიმატების, გამოკლების, გამრავლებისა და გაყოფის მეთოდებით

# შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.

class Calculator:
    @staticmethod
    def add():
        inp_nums_add = [int(num) for num in input("Enter numbers to add, separated by commas: ").split(',')]
        result = sum(inp_nums_add)
        print("Result:", result)

    @staticmethod
    def subtract():
        inp_nums_sub = [int(num) for num in input("Enter numbers to subtract, separated by commas: ").split(',')]
        result = inp_nums_sub[0]
        for num in inp_nums_sub[1:]:
            result -= num
            print("Result:", result)

    @staticmethod
    def multiply():
        inp_nums_mul = [int(num) for num in input("Enter numbers to multiply, separated by commas: ").split(',')]
        result = 1
        for num in inp_nums_mul:
            result *= num
        print("Result:", result)

    @staticmethod
    def divide():
        inp_nums_div = [int(num) for num in input("Enter numbers to divide, separated by commas: ").split(',')]
        result = inp_nums_div[0]
        for num in inp_nums_div[1:]:
            if num != 0:
                result /= num
            else:
                print("Error: Cannot divide by zero.")
                return None
        print("Result:", result)

Calculator.add()
Calculator.subtract()
Calculator.multiply()
Calculator.divide()

# არასავალდებულო დავალება - შოფინგ ქართის შექმნა - რატომღაც მგონია, რომ უფრო ადვილადაც შემეძლო ამის გაკეთება, მაგრამ ვერ ვხვდები ზუსტად სად. 

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'quantity': quantity, 'price': price}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"{item} removed from the cart.")
        else:
            print(f"{item} is not in the cart.")

    def display_cart(self):
        print("Shopping Cart:")
        for item, details in self.items.items():
            print(f"{item}: Quantity - {details['quantity']}, Price per unit - ${details['price']}")

    def calculate_total(self):
        total_cost = sum(details['quantity'] * details['price'] for details in self.items.values())
        print(f"Total Cost: ${total_cost:.2f}")

cart = ShoppingCart()

cart.add_item("Laptop", 1200, 2)
cart.add_item("Mouse", 20)
cart.add_item("Keyboard", 50, 3)

cart.display_cart()
cart.calculate_total()

cart.remove_item("Mouse")

cart.display_cart()
cart.calculate_total()
