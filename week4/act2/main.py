from land import Land


def main():

    land = Land(4.5, 3)

    print(f"Land area: {land.calculate_area()}")
    print(f"Land perimeter: {land.calculate_perimeter()}")
    land.print_dimensions()

if __name__ == "__main__":
    main()
