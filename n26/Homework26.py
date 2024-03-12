# 1 Single Responsibility principle

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Storage:
    def save_user(self, user):
        # Logic to save the user to storage
        pass


class HttpConnection:
    def send_data(self, data):
        # Logic to send data over HTTP connection
        pass


class Logger:
    def log_message(self, message):
        # Logic to log messages
        pass


# Open-Closed principle

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favourite':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4
        else:
            return self.price  # No discount for other customers


class VIPDiscount(Discount):
    def give_discount(self):
        return super().give_discount()  # VIP customers get the discount defined in the parent class


# Example usage:
regular_discount = Discount('favourite', 100)
vip_discount = VIPDiscount('vip', 100)

print("Regular discount:", regular_discount.give_discount())  # Output: 20.0
print("VIP discount:", vip_discount.give_discount())  # Output: 40.0
