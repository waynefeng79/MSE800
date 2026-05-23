# Auckland Aquarium Manager

This project manages a small aquarium inventory in Auckland for the following fish species:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

It demonstrates both the Factory and Singleton design patterns:

- `FishFactory` produces fish objects based on categories.
- `Aquarium` is a singleton inventory manager.

## Features

- Accepts user input for fish category and quantity.
- Stores fish count in a local SQLite database.
- Displays the fish category and current available count.
- Includes a database design that supports extendable categories.

## Project Files

- `aquarium.py` - Library containing the `Aquarium` manager class.
- `main.py` - CLI entrypoint that uses `Aquarium`.
- `fish.py` - Fish base class and concrete fish types.
- `fish_factory.py` - Factory that creates fish objects by category.
- `database.py` - Database connection manager.

## Database Table Design

The aquarium uses two tables:

- `fish_categories` stores category metadata.
- `fish_inventory` stores the count for each category.

## Usage

Run the application with:

```bash
python main.py
```

Follow the prompts and enter a category from the supported list, then a quantity to add. Leave the category blank to exit.