import unittest
from src.character_factory import KnightFactory, TrollFactory
from src.weapons import KnifeBehavior
from src.characters import CharacterObserver

class MockObserver(CharacterObserver):
    def __init__(self):
        self.last_health = None

    def update(self, character_name: str, health: int) -> None:
        self.last_health = health

class TestGameEngine(unittest.TestCase):
    def test_factory_method_creates_knight(self):
        factory = KnightFactory()
        knight = factory.create_character("Lancelot")
        self.assertEqual(knight.health, 100)
        self.assertIn("Knight", knight.describe())

    def test_strategy_attack_and_switch(self):
        factory = TrollFactory()
        troll = factory.create_character("Grag")
        self.assertIn("arrow", troll.perform_attack())
        
        troll.set_weapon(KnifeBehavior())
        self.assertIn("dagger", troll.perform_attack())

    def test_observer_notified_on_damage(self):
        factory = KnightFactory()
        knight = factory.create_character("Galahad")
        observer = MockObserver()
        knight.register_observer(observer)
        
        knight.take_damage(30)
        self.assertEqual(knight.health, 70)
        self.assertEqual(observer.last_health, 70)

if __name__ == "__main__":
    unittest.main()