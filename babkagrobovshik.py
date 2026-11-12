
class Streamer:
    def __init__(self, nick, followers):
        self.nick = nick
        self.donates = []  
        self.followers = followers

    def add_donate(self, amount):
        self.donates.append(amount)

    def total_donates(self):
        return sum(self.donates)

    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return sum(self.donates) / len(self.donates)

def print_stats(streamer):
    print("\n=== Статистика стримера ===")
    print("Ник:", streamer.nick)
    print("Подписчики:", streamer.followers)
    print("Всего донатов:", streamer.total_donates())
    print("Средний донат:", streamer.average_donate())


class GameCharacter:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
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
    print("\n=== Статистика персонажа ===")
    print("Имя:", hero.name)
    print("Уровень:", hero.level)
    print("Здоровье:", hero.health)
    print("Инвентарь:", hero.inventory)


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = [] 

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

def print_student(student):
    print("\n=== Информация о студенте ===")
    print("Имя:", student.name)
    print("Группа:", student.group)
    print("Оценки:", student.grades)
    print("Средний балл:", student.average_grade())



if __name__ == "__main__":
 
    streamer = Streamer("GolubKin", 1200)
    streamer.add_donate(500)
    streamer.add_donate(150)
    print_stats(streamer)

    
    hero = GameCharacter("Артас", 80, 100)
    hero.add_item("Меч")
    hero.add_item("Щит")
    hero.take_damage(30)
    hero.heal(10)
    print_character(hero)

    student = Student("оля цымбал", "26КАДР-1")
    student.add_grade(5)
    student.add_grade(4)
    student.add_grade(5)
    print_student(student)