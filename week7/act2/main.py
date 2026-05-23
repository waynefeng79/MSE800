from aquarium import Aquarium

def run_cli():
    aquarium = Aquarium()
    aquarium = Aquarium()
    aquarium.display_inventory()

    supported_categories = aquarium.get_supported_categories()
    print("Enter fish category and quantity to add to the Auckland aquarium.")
    print(f"Supported categories: {', '.join(supported_categories)}")

    while True:
        category = input("Category (blank to exit): ").strip()
        if not category:
            break

        try:
            quantity = int(input("Quantity to add: ").strip())
        except ValueError:
            print("Please enter a valid whole number for quantity.\n")
            continue

        try:
            info = aquarium.add_fish(category, quantity)
            print(
                f"Added {quantity} {info['category']}. "
                f"Current count: {info['count']}\n"
            )
            aquarium.display_inventory()
        except ValueError as exc:
            print(f"Error: {exc}\n")

    print("Exiting the Auckland Aquarium Manager.")

if __name__ == "__main__":
    run_cli()
