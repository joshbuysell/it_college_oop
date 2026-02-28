# Звіт до роботи
## Тема: Основні парадигми ООП
### Мета роботи: Ознайомитись з ключовими поняттями об'єктно-орієнтованого програмування (ООП) у Python та навчитися реалізовувати їх у власних класах на прикладі ігрової симуляції.

---

## Виконання роботи

### 1. Інкапсуляція

Клас `BankAccount` з приватним атрибутом `__balance` та методами `deposit`, `withdraw`, `get_balance`:

```python
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
```

**Завдання 1:** Додано генератор випадкових чисел та виклик `deposit`/`withdraw` у циклі:

```python
import random

account2 = BankAccount("Viktor", 5000)
for i in range(10):
    operation = random.choice(["deposit", "withdraw"])
    amount = random.randint(100, 1000)
    if operation == "deposit":
        account2.deposit(amount)
    else:
        account2.withdraw(amount)
```

Початковий баланс 5000, після 10 випадкових операцій (deposit/withdraw з сумами 100-1000) баланс змінюється кожен раз по-різному.

---

### 2. Наслідування

Класи `Vehicle` та `Car`, де `Car` наслідує `Vehicle`:

```python
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
```

**Завдання 2:** Створив метод `honk()` у класі `Vehicle` та викликав його з об'єкта `Car`:

```
Toyota Camry, Seats: 5
Toyota Camry сигналить: Біп-біп!
```

Дочірній клас автоматично наслідує всі методи батьківського.

---

### 3. Поліморфізм

Класи `Animal`, `Dog`, `Cat` з методом `speak()`:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

**Завдання 3:** Клас `Fish` без методу `speak`:

```python
class Fish(Animal):
    pass
```

Результат виконання:
```
Dog.speak() -> Woof!
Cat.speak() -> Meow!
Fish.speak() -> None
```

`Fish.speak()` повертає `None` бо метод успадкований від `Animal` який має `pass`. Помилки не буде, просто нічого не поверне.

---

### 4. Абстракція

Абстрактний клас `Shape` з модулем `abc`:

```python
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
```

Площа кола (r=5): 78.5. Спроба створити `Shape()` напряму кидає `TypeError`.

---

### 5. Ігрова симуляція (базовий приклад)

Базова гра між мечем та сокирою, де використовуються всі 4 парадигми:

| Парадигма | Реалізація | Опис |
|---|---|---|
| Абстракція | `class Item(ABC)` + `@abstractmethod attack()` | Задає спільний інтерфейс для усіх типів зброї |
| Наслідування | `class Sword(Item)` | Використовує атрибути і методи базового класу |
| Інкапсуляція | `__attack_power`, `_sharp`, `@property` | Обмежує прямий доступ до внутрішніх змінних |
| Поліморфізм | `attack()` перевизначений у `Sword` і `Axe` | Метод має однакове ім'я, але різну поведінку |

---

### 6. Головне завдання: Bow + випадковий вибір + покрокова гра

Третій тип зброї — **Bow (лук)**:

```python
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
    
    def reload(self):
        self.__range_power += 1
        self._boost_next = True
```

Що зроблено:
- Клас `Bow` з параметром `range_power` та формулою `attack_power + randint(5, 15) + range_power`
- Метод `reload()` який збільшує `range_power += 1`
- Функція `create_random_weapon()` для випадкового вибору зброї
- `play_auto_game()` — автоматична гра між двома випадковими типами зброї
- `play_interactive_game()` — покрокова гра де можна обирати дію (атака/підсилення)

---

## Висновок

Розібрався з основними парадигмами ООП — інкапсуляція, наслідування, поліморфізм, абстракція. Написав приклади для кожної. Зробив завдання з BankAccount (рандомні операції), Vehicle/Car (наслідування методів), Fish (поведінка без перевизначення speak), ну і головне — ігрову симуляцію з трьома типами зброї (Sword, Axe, Bow). Лук має reload для дальності, є рандомний вибір зброї і покрокова гра з вибором дій. З нового для себе — абстрактні класи через ABC, name mangling для приватних атрибутів, property. Все працює, складностей не було.
