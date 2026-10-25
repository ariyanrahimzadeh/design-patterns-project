from abc import ABC, abstractmethod

# Pattern: Strategy | Role: Strategy (Interface)
class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self) -> str:
        """Returns the attack action message of the weapon."""
        pass

# Pattern: Strategy | Role: ConcreteStrategy
class SwordBehavior(WeaponBehavior):
    def use_weapon(self) -> str:
        return "slashed with a sharp sword!"

# Pattern: Strategy | Role: ConcreteStrategy
class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self) -> str:
        return "shot an arrow with high precision!"

# Pattern: Strategy | Role: ConcreteStrategy
class KnifeBehavior(WeaponBehavior):
    def use_weapon(self) -> str:
        return "made a swift strike with a dagger!"