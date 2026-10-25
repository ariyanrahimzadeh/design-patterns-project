from abc import ABC, abstractmethod
from typing import List
from src.weapons import WeaponBehavior

# Pattern: Observer | Role: Observer (Interface)
class CharacterObserver(ABC):
    @abstractmethod
    def update(self, character_name: str, health: int) -> None:
        pass

# Pattern: Strategy | Role: Context
# Pattern: Observer | Role: Subject
class Character(ABC):
    def __init__(self, name: str, health: int, weapon: WeaponBehavior):
        self.name = name
        self.health = health
        self._weapon = weapon
        self._observers: List[CharacterObserver] = []

    def set_weapon(self, weapon: WeaponBehavior) -> None:
        """Changes the attack strategy dynamically at runtime."""
        self._weapon = weapon

    def perform_attack(self) -> str:
        return f"{self.name} -> {self._weapon.use_weapon()}"

    def register_observer(self, observer: CharacterObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: CharacterObserver) -> None:
        self._observers.remove(observer)

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)
        self._notify_observers()

    def _notify_observers(self) -> None:
        for obs in self._observers:
            obs.update(self.name, self.health)

    @abstractmethod
    def describe(self) -> str:
        pass

# Somut Karakter Sınıfları
class Knight(Character):
    def describe(self) -> str:
        return f"Knight {self.name} (Health: {self.health})"

class Troll(Character):
    def describe(self) -> str:
        return f"Troll {self.name} (Health: {self.health})"