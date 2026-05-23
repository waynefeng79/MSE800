class Fish:
    def __init__(self, category: str):
        self.category = category

class Goldfish(Fish):
    def __init__(self):
        super().__init__(category="Goldfish")

class Shark(Fish):
    def __init__(self):
        super().__init__(category="Shark")

class Angelfish(Fish):
    def __init__(self):
        super().__init__(category="Angelfish")

class Tuna(Fish):
    def __init__(self):
        super().__init__(category="Tuna")

class Salmon(Fish):
    def __init__(self):
        super().__init__(category="Salmon")
