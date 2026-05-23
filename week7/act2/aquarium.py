from database import DatabaseConnection
from fish_factory import SimpleFishFactory

class Singleton:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            print("Create Singleton instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

class Aquarium(Singleton):
    def __init__(self, db_path: str = "aquarium.db"):
        self._initialized = getattr(self, "_initialized", False)
        if self._initialized:
            return
        print("Initializing Aquarium instance...")
        self.db = DatabaseConnection(db_path).connection
        self.fish_factory = SimpleFishFactory()
        self._ensure_schema()
        self._seed_categories()
        self._initialized = True

    def _ensure_schema(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS fish_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL UNIQUE,
                location TEXT NOT NULL DEFAULT 'Auckland'
            );
            """
        )
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS fish_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL UNIQUE,
                count INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (category_id) REFERENCES fish_categories(id)
            );
            """
        )
        self.db.commit()

    def _seed_categories(self):
        supported = ["Goldfish", "Shark", "Angelfish", "Tuna", "Salmon"]
        cursor = self.db.cursor()
        for category in supported:
            fish = self.fish_factory.create_fish(category)
            cursor.execute(
                "INSERT OR IGNORE INTO fish_categories (category, location) VALUES (?, ?)",
                (fish.category, "Auckland"),
            )
        self.db.commit()

        cursor.execute("SELECT id FROM fish_categories")
        for row in cursor.fetchall():
            cursor.execute(
                "INSERT OR IGNORE INTO fish_inventory (category_id, count) VALUES (?, 0)",
                (row["id"],),
            )
        self.db.commit()

    def _ensure_category_registration(self, fish):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO fish_categories (category, location) VALUES (?, ?)",
            (fish.category, "Auckland"),
        )
        self.db.commit()
        cursor.execute(
            "SELECT id FROM fish_categories WHERE category = ?",
            (fish.category,),
        )
        category_id = cursor.fetchone()["id"]
        cursor.execute(
            "INSERT OR IGNORE INTO fish_inventory (category_id, count) VALUES (?, 0)",
            (category_id,),
        )
        self.db.commit()
        return category_id

    def add_fish(self, category: str, quantity: int) -> dict:
        fish = self.fish_factory.create_fish(category)
        category_id = self._ensure_category_registration(fish)
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE fish_inventory SET count = count + ? WHERE category_id = ?",
            (quantity, category_id),
        )
        self.db.commit()
        cursor.execute(
            "SELECT c.category, i.count"
            " FROM fish_inventory i"
            " JOIN fish_categories c ON i.category_id = c.id"
            " WHERE c.id = ?",
            (category_id,),
        )
        row = cursor.fetchone()
        return dict(row)

    def get_fish_info(self, category: str) -> dict:
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT c.category, i.count"
            " FROM fish_inventory i"
            " JOIN fish_categories c ON i.category_id = c.id"
            " WHERE c.category = ?",
            (category.strip().title(),),
        )
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"Category '{category}' not found in inventory.")
        return dict(row)

    def get_supported_categories(self) -> list[str]:
        cursor = self.db.cursor()
        cursor.execute("SELECT category FROM fish_categories ORDER BY category")
        return [row["category"] for row in cursor.fetchall()]

    def display_inventory(self):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT c.category, i.count"
            " FROM fish_inventory i"
            " JOIN fish_categories c ON i.category_id = c.id"
            " ORDER BY c.category"
        )
        rows = cursor.fetchall()
        print("\nAuckland Aquarium Inventory")
        print("---------------------------")
        for row in rows:
            print(f"{row['category']}: {row['count']}")
        print()
