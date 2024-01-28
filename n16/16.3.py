# შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები სასურველი ნივთის დასამატებლად და ამოსაშლელად, ასევე კალათაში არსებული პროდუქტების სიისა და ჯამური ღირებულების გამოსატანად.

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
