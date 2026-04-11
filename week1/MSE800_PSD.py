import sys

print(sys.executable)
print(sys.version)

def calc_power(x, y):
    return x ** y

def main():
    x = 2
    y = 4
    z = calc_power(x, y)
    print(f"power({x}, {y}) = {z}")

if __name__ == "__main__":
    main()
