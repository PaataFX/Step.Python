registered_users = []

name = input("Enter your username: ")
password = input("Enter your password (at least 8 characters): ")

if name and len(password) >= 8:
    registered_users.append([name, password])
    print("Registration successful!")
else:
    print("Registration failed. Username should not be empty, and the password should be at least 8 characters.")

login_name = input("Enter your username ")
login_password = input("Enter your password: ")

login_successful = any(user[0] == login_name and user[1] == login_password for user in registered_users)

if login_successful:
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")
