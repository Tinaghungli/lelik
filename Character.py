class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def add_item(self, item):
        self.inventory.append(item)

def print_character(hero):
    print(f"Персонаж: {hero.name}")
    print(f"Уровень: {hero.level}, здоровье: {hero.health}")
    print(f"Инвентарь: {hero.inventory}")

def is_alive(hero):
    return hero.health > 0

print("\n--- ВАРИАНТ 2 ---")
hero = Character("Genshin_Hero", 42)
hero.add_item("Меч дождя")
hero.add_item("Крылышки ветра")
hero.take_damage(30)
hero.heal(10)
print_character(hero)
print("Жив:", is_alive(hero))