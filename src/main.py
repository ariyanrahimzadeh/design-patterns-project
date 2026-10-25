from src.character_factory import KnightFactory, TrollFactory
from src.weapons import KnifeBehavior
from src.characters import CharacterObserver

# Pattern: Observer | Role: ConcreteObserver
class HealthHUD(CharacterObserver):
    def update(self, character_name: str, health: int) -> None:
        print(f"[HUD UPDATE] {character_name}'s current health: {health}")

def main():
    print("=== Game Character Engine Started ===")
    
    # 1. Factory Method ile üretim
    knight_factory = KnightFactory()
    arthur = knight_factory.create_character("Arthur")
    
    # 2. Observer kaydı
    hud = HealthHUD()
    arthur.register_observer(hud)
    
    # 3. Strategy kullanımı
    print(arthur.describe())
    print(arthur.perform_attack())
    
    # 4. Strategy dinamik değişimi
    print("\n--- Arthur switches weapon ---")
    arthur.set_weapon(KnifeBehavior())
    print(arthur.perform_attack())
    
    # 5. Hasar alma ve Observer tetiklenmesi
    print("\n--- Arthur takes damage ---")
    arthur.take_damage(25)

if __name__ == "__main__":
    main()