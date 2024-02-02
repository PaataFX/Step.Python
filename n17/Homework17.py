class ParentClass:
    def __init__(self, public_param, protected_param, private_param):
        self.public_param = public_param
        self._protected_param = protected_param
        self.__private_param = private_param

    @property
    def public_param(self):
        return self._public_param

    @public_param.setter
    def public_param(self, value):
        self._public_param = value

    @property
    def protected_param(self):
        return self._protected_param

    @protected_param.setter
    def protected_param(self, value):
        self._protected_param = value

    @property
    def private_param(self):
        return self.__private_param

    @private_param.setter
    def private_param(self, value):
        self.__private_param = value


class ChildClass(ParentClass):
    def __init__(self, public_param, protected_param, private_param, additional_param):
        super().__init__(public_param, protected_param, private_param)
        self.additional_param = additional_param

    @property
    def public_param(self):
        return f"ChildClass - {self._public_param}"

    def new_method(self):
        print("This is a new method in the ChildClass.")

parent_instance = ParentClass(public_param=1, protected_param=2, private_param=3)

print(parent_instance.public_param)  # Output: 1
parent_instance.public_param = 42
print(parent_instance.public_param)  # Output: 42

child_instance = ChildClass(public_param=10, protected_param=20, private_param=30, additional_param=40)

print(child_instance.public_param)  # Output: ChildClass - 10
child_instance.public_param = 99
print(child_instance.public_param)  # Output: ChildClass - 99

child_instance.new_method()  # Output: This is a new method in the ChildClass.
