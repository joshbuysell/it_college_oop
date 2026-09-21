"""
Основні парадигми ООП
"""

# 1. Інкапсуляція

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance


account = BankAccount("Bohdan", 1000)
account.deposit(500)
print(f"Баланс після депозиту: {account.get_balance()}")

# Завдання 1: deposit/withdraw у циклі з рандомом
import random

account2 = BankAccount("Viktor", 5000)
print(f"Початковий баланс: {account2.get_balance()}")

for i in range(10):
    operation = random.choice(["deposit", "withdraw"])
    amount = random.randint(100, 1000)
    
    if operation == "deposit":
        account2.deposit(amount)
        print(f"  Крок {i+1}: deposit +{amount}, баланс = {account2.get_balance()}")
    else:
        result = account2.withdraw(amount)
        if result == "Insufficient funds":
            print(f"  Крок {i+1}: withdraw -{amount} -> Недостатньо коштів! Баланс = {account2.get_balance()}")
        else:
            print(f"  Крок {i+1}: withdraw -{amount}, баланс = {account2.get_balance()}")

print(f"Кінцевий баланс: {account2.get_balance()}")


# 2. Наслідування

print("\n" + "="*60)
print("2. Наслідування")
print("="*60)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"
    
    def honk(self):
        return f"{self.brand} {self.model} сигналить: Біп-біп!"


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"


car = Car("Toyota", "Camry", 5)
print(car.display_info())
print(car.honk())


# 3. Поліморфізм

print("\n" + "="*60)
print("3. Поліморфізм")
print("="*60)

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    pass

animals = [Dog(), Cat(), Fish()]
for animal in animals:
    result = animal.speak()
    print(f"{animal.__class__.__name__}.speak() -> {result}")

print("\nFish.speak() повертає None бо метод успадкований від Animal з pass")


# 4. Абстракція

print("\n" + "="*60)
print("4. Абстракція")
print("="*60)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Площа кола (r=5): {circle.area()}")
print(f"Площа прямокутника (4x6): {rectangle.area()}")

try:
    s = Shape()
except TypeError as e:
    print(f"Помилка створення Shape(): {e}")


# 5. Ігрова симуляція — базовий приклад

print("\n" + "="*60)
print("5. Ігрова симуляція")
print("="*60)

from random import randint

class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self):
        pass


class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"Удар мечем {self.name}, шкода {current_attack}. У {another_item.name} HP: {another_item.health}"
    
    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp}"
    
    def sharpening(self):
        self._sharp += 1


class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"Удар сокирою {self.name}, шкода {current_attack}. У {another_item.name} HP: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp}"


S = Sword("Ескалібур", 100)
A = Axe("Кратос", 95)

for i in range(10):
    print(f"\nХід {i + 1}")
    
    S.sharpening()
    print(S.attack(A))
    if A.health <= 0:
        print(f"Перемога за {S.name}!")
        break
    
    print(A.attack(S))
    if S.health <= 0:
        print(f"Перемога за {A.name}!")
        break


# 6. Головне завдання: Bow + випадковий вибір + покрокова гра

print("\n" + "="*60)
print("Розширена ігрова симуляція")
print("="*60)


class GameItem(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health
        self._boost_next = False
    
    @abstractmethod
    def attack(self, another_item):
        pass
    
    @abstractmethod
    def boost(self):
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        pass
    
    def is_alive(self):
        return self.health > 0


class GameSword(GameItem):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
    
    def attack(self, another_item: GameItem):
        bonus = 5 if self._boost_next else 0
        self._boost_next = False
        current_attack = self.__attack_power + self._sharp + randint(0, 10) + bonus
        another_item.health -= current_attack
        return current_attack
    
    def boost(self):
        self._sharp += 1
        self._boost_next = True
        return f"{self.name} загострено! Гострота: {self._sharp}, +5 до наступного удару"
    
    def get_info(self):
        return f"Меч '{self.name}' | HP: {self.health} | Атака: {self.__attack_power + self._sharp}"


class GameAxe(GameItem):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
    
    def attack(self, another_item: GameItem):
        bonus = 8 if self._boost_next else 0
        self._boost_next = False
        current_attack = self.__attack_power + self._sharp + randint(0, 20) + bonus
        another_item.health -= current_attack
        return current_attack
    
    def boost(self):
        self._sharp += 2
        self._boost_next = True
        return f"{self.name} заточено! Гострота: {self._sharp}, +8 до наступного удару"
    
    def get_info(self):
        return f"Сокира '{self.name}' | HP: {self.health} | Атака: {self.__attack_power + self._sharp}"


class Bow(GameItem):
    def __init__(self, name, attack_power: int, range_power: int = 10):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.__range_power = range_power
    
    def attack(self, another_item: GameItem):
        bonus = 3 if self._boost_next else 0
        self._boost_next = False
        current_attack = self.__attack_power + randint(5, 15) + self.__range_power + bonus
        another_item.health -= current_attack
        return current_attack
    
    def boost(self):
        self.__range_power += 1
        self._boost_next = True
        return f"{self.name} перезаряджено! Дальність: {self.__range_power}, +3 до наступного удару"
    
    def reload(self):
        return self.boost()
    
    def get_info(self):
        return f"Лук '{self.name}' | HP: {self.health} | Атака: {self.__attack_power} | Дальність: {self.__range_power}"


def create_random_weapon():
    weapons = [
        lambda: GameSword("Ескалібур", randint(80, 120)),
        lambda: GameAxe("Кратос", randint(75, 115)),
        lambda: Bow("Робін Гуд", randint(70, 100), randint(5, 15)),
    ]
    return random.choice(weapons)()


def play_auto_game():
    print("\nАвтоматична гра")
    print("=" * 50)
    weapon1 = create_random_weapon()
    weapon2 = create_random_weapon()
    
    print(f"Гравець 1: {weapon1.get_info()}")
    print(f"Гравець 2: {weapon2.get_info()}")
    
    turn = 0
    while weapon1.is_alive() and weapon2.is_alive():
        turn += 1
        print(f"\n--- Хід {turn} ---")
        
        if randint(0, 1) == 0:
            print(weapon1.boost())
        dmg = weapon1.attack(weapon2)
        print(f"  {weapon1.name} -> {weapon2.name}: {dmg} шкоди. HP {weapon2.name}: {weapon2.health}")
        if not weapon2.is_alive():
            print(f"\nПеремога за {weapon1.name}! (Хід {turn})")
            break
        
        if randint(0, 1) == 0:
            print(weapon2.boost())
        dmg = weapon2.attack(weapon1)
        print(f"  {weapon2.name} -> {weapon1.name}: {dmg} шкоди. HP {weapon1.name}: {weapon1.health}")
        if not weapon1.is_alive():
            print(f"\nПеремога за {weapon2.name}! (Хід {turn})")
            break
    
    return weapon1, weapon2


def play_interactive_game():
    print("\n" + "="*50)
    print("  ПОКРОКОВА ІГРОВА СИМУЛЯЦІЯ")
    print("="*50)
    
    print("\nОберіть свою зброю:")
    print("  1. Меч (середня атака, загострювання +5)")
    print("  2. Сокира (висока варіативність, заточка +8)")
    print("  3. Лук (дальній бій, перезарядка +3)")
    
    choice = input("\nВаш вибір (1/2/3): ").strip()
    
    if choice == "1":
        player = GameSword("Ескалібур", 100)
    elif choice == "2":
        player = GameAxe("Кратос", 95)
    elif choice == "3":
        player = Bow("Робін Гуд", 85, 10)
    else:
        print("Невірний вибір, обрано меч")
        player = GameSword("Ескалібур", 100)
    
    enemy = create_random_weapon()
    
    print(f"\nВаша зброя: {player.get_info()}")
    print(f"Суперник:   {enemy.get_info()}")
    
    turn = 0
    while player.is_alive() and enemy.is_alive():
        turn += 1
        print(f"\n{'='*40}")
        print(f"  Хід {turn}")
        print(f"{'='*40}")
        print(f"Ви: HP={player.health}  |  Суперник: HP={enemy.health}")
        print("\nОберіть дію:")
        print("  1. Атакувати")
        print("  2. Підсилити зброю + атакувати")
        
        action = input("Ваш вибір (1/2): ").strip()
        
        if action == "2":
            print(player.boost())
        
        dmg = player.attack(enemy)
        print(f"  Ви атакуєте на {dmg} шкоди! HP суперника: {enemy.health}")
        
        if not enemy.is_alive():
            print(f"\nПеремога! Ви перемогли за {turn} ходів!")
            break
        
        if randint(0, 2) == 0:
            enemy.boost()
        dmg = enemy.attack(player)
        print(f"  Суперник атакує на {dmg} шкоди! Ваше HP: {player.health}")
        
        if not player.is_alive():
            print(f"\nПоразка! Суперник переміг на ході {turn}.")
            break
    
    print("\n--- Гра завершена ---")


print("\nЗапуск автоматичної гри з випадковими типами зброї:")
play_auto_game()

# play_interactive_game()
