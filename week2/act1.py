def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    return x / y

def mod(x, y):
    return x % y

def factor(x, y):
    return x ** y

def main():
    x = complex(input("input x: "))
    y = complex(input("input y: "))

    op = input("operation(add/minus/multi/divide/mod/factor): ")
    match op:
        case "add":
            print(f"{x} + {y} = {add(x, y)}")
        case "minus":
            print(f"{x} - {y} = {minus(x, y)}")
        case "multi":
            print(f"{x} * {y} = {multi(x, y)}")
        case "divide":
            print(f"{x} / {y} = {divide(x, y)}")
        case "mod":
            print(f"{x} % {y} = {complex(mod(x.real, int(y.real)), mod(x.imag, int(y.real)))}")
        case "factor":
            print(f"{x} factor {y} = {factor(x, y)}")

if __name__ == "__main__":
    main()