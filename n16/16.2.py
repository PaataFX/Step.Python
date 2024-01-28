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
