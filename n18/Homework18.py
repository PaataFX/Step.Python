class BankAccount:
    def __init__(self, username, password, initial_amount=0):
        self.username = username
        self._password = self._validate_password(password)
        self.balance = initial_amount

    def _validate_password(self, password):
        if len(password) >= 8:
            return password
        else:
            raise ValueError("Password must have a minimum of 8 characters.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            return f"Transferred ${amount} to {recipient.username}. Your new balance: ${self.balance}"
        else:
            return "Invalid transfer amount or insufficient funds."

    def __repr__(self):
        return f"BankAccount(username='{self.username}', balance=${self.balance})"


account1 = BankAccount(username="user1", password="securepassword", initial_amount=1000)
account2 = BankAccount(username="user2", password="strongpass", initial_amount=500)

# Deposit money
print(account1.deposit(200))  # Output: Deposited $200. New balance: $1200

# Withdraw money
print(account1.withdraw(100))  # Output: Withdrew $100. New balance: $1100

# Transfer money
print(account1.transfer(account2, 300))  # Output: Transferred $300 to user2. Your new balance: $800

# Display account information using __repr__
print(account1)  # Output: BankAccount(username='user1', balance=$800)
print(account2)  # Output: BankAccount(username='user2', balance=$800)
