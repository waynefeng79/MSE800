class Calculator:
    def __init__(self):
        self.error = None

    def print_result1(self, op, x, z):
        if self.error:
            print(f"{x}{op} error: {self.error}")
        else:
            print(f"{x}{op} = {z}")

    def print_result2(self, op, x, y, z):
        if self.error:
            print(f"{x} {op} {y} error: {self.error}")
        else:
            print(f"{x} {op} {y} = {z}")

    def add(self, x, y):
        z = x + y
        self.print_result2("+", x, y, z)
        return z

    def minus(self, x, y):
        z = x - y
        self.print_result2("-", x, y, z)
        return z

    def multi(self, x, y):
        z = x * y
        self.print_result2("*", x, y, z)
        return z

    def divide(self, x, y):
        if y == 0:
            self.error = "Divide by zero"
            z = -1
        else:
            z = x / y
        self.print_result2("/", x, y, z)
        self.error = None
        return z

    def mod(self, x, y):
        if y == 0:
            self.error = "Modulo by zero"
            z = -1
        elif type(x) is complex or type(y) is complex:
            self.error = "Complex not supported"
            z = -1
        else:
            z = x % y
        self.print_result2("%", x, y, z)
        self.error = None
        return z

    def factorial(self, x):
        if type(x) is not int:
            self.error = f"{type(x).__name__} not supported"
            z = -1
        elif x < 0:
            self.error = "Negative not supported"
            z = -1
        else:
            z = 1
            for i in range(2, x + 1):
                z *= i
        self.print_result1("!", x, z)
        self.error = None
        return z

def input_operation():
    while True:
        print("Operations:")
        print("1. add")
        print("2. minus")
        print("3. multiply")
        print("4. divide")
        print("5. modulo")
        print("6. factorial")
        print("7. quit")
        try:
            choice = int(input("Select(1/2/3/4/5/6/7): "))
            if choice >= 1 and choice <= 7:
                break
        except ValueError:
            print("Wrong operation, try again...")

    return choice

def input_number(var):
    while True:
        s = input(f"{var} = ")
        try:
            v = int(s)
            break
        except ValueError:
            pass

        try:
            v = float(s)
            break
        except ValueError:
            pass

        try:
            v = complex(s)
            break
        except ValueError:
            pass

        print(f"Wrong number {s}, try again...")

    return v

def main():
    print("== Calculator application: ==")
    
    calc = Calculator()

    while True:
        print()
        op = input_operation()
        if op == 7:
            break

        x = input_number("x")
        if op != 6:
            y = input_number("y")
        
        match op:
            case 1:
                calc.add(x, y)
            case 2:
                calc.minus(x, y)
            case 3:
                calc.multi(x, y)
            case 4:
                calc.divide(x, y)
            case 5:
                calc.mod(x, y)
            case 6:
                calc.factorial(x)

if __name__ == "__main__":
    main()