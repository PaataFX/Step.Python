class Employee:
    raise_amount = 1.05

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @property
    def email(self):
        return f'{self.firstname[0].lower()}.{self.lastname.lower()}@gmail.com'

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


# employee1 = Employee("Nika", "Khorguani", 4000)
# print(employee1.email)
# print(employee1.full_name)
# # print(employee1.salary)
# employee1.apply_raise()
# # print(employee1.salary)