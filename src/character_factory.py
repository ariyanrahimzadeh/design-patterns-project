from abc import ABC, abstractmethod
from src.characters import Character, Knight, Troll
from src.weapons import SwordBehavior, BowAndArrowBehavior

# Pattern: Factory Method | Role: Creator (Interface)
class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self, name: str) -> Character:
        pass

# Pattern: Factory Method | Role: ConcreteCreator
class KnightFactory(CharacterFactory):
    def create_character(self, name: str) -> Character:
        return Knight(name=name, health=100, weapon=SwordBehavior())

# Pattern: Factory Method | Role: ConcreteCreator
class TrollFactory(CharacterFactory):
    def create_character(self, name: str) -> Character:
        return Troll(name=name, health=150, weapon=BowAndArrowBehavior())