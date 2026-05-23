from fish import Angelfish, Fish, Goldfish, Salmon, Shark, Tuna

from abc import ABC, abstractmethod

class FishFactory(ABC):
    @abstractmethod
    def create_fish(self, category: str) -> Fish:
        """Create and return a `Fish` instance."""
        pass

class SimpleFishFactory(FishFactory):
    def create_fish(self, category: str) -> Fish:
        if category == "Goldfish":
            return Goldfish()
        elif category == "Shark":
            return Shark()
        elif category == "Angelfish":
            return Angelfish()
        elif category == "Tuna":
            return Tuna()
        elif category == "Salmon":
            return Salmon()
        else:
            raise ValueError(f"Unsupported fish category: {category}")