class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Current balance for account of {self.account_holder}: ${self.balance:.2f}")


def create_profile():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    return username, password


def login(profiles):
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    return entered_username, entered_password


def main():
    profiles = {}

    while True:
        print("\n1. Create a profile")
        print("2. Login")
        print("3. Deposit money")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            username, password = create_profile()
            profiles[username] = {'password': password, 'account': BankAccount(username)}

        elif choice == '2':
            entered_username, entered_password = login(profiles)

            try:
                profile = profiles[entered_username]
                if entered_password == profile['password']:
                    print("\nLogin successful!")
                    profile['account'].display_balance()
                else:
                    raise ValueError("Incorrect password. Please try again.")
            except KeyError:
                print("Username not found. Please create a profile.")
            except ValueError as e:
                print(e)

        elif choice == '3':
            entered_username, _ = login(profiles)

            try:
                profile = profiles[entered_username]
                deposit_amount = float(input("Enter the deposit amount: $"))
                profile['account'].deposit(deposit_amount)
            except KeyError:
                print("Username not found. Please create a profile.")
            except ValueError:
                print("Invalid input for deposit amount. Please enter a valid number.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
