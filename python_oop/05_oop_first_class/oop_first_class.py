class MyName:
    """Опис класу / Документація"""

    total_names = 0  # Class Variable

    def __init__(self, name=None, domain="itcollege.lviv.ua"):
        """Ініціалізація класу"""
        if name is None:
            name = self.anonymous_user().name
        # Перевірка на валідність імені
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        self.name = name.capitalize()  # Завжди з великої літери
        self.domain = domain
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        """Class property: повертаємо ім'я"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property: повертаємо емейл"""
        return self.create_email()

    def create_email(self) -> str:
        """Instance method: створює email"""
        return f"{self.name.lower()}@{self.domain}"

    @classmethod
    def anonymous_user(cls):
        """Class method: створює анонімного користувача"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method: повертає привітання"""
        return f"You say: {message}"

    @property
    def full_name(self) -> str:
        """Повертає повну інформацію про користувача"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def count_letters(self) -> int:
        """Повертає кількість букв у імені"""
        return len(self.name)

    def save_to_file(self, filename="users.txt"):
        """Додає рядок із записом у файл"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")


# --- Демонстрація роботи ---
print("Розпочинаємо створювати об'єкти!")

names = ("Bohdan", "Marta", "Viktor", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"{" >*< "*20}")
    print(f"This is object: {me}")
    print(f"This is object attribute: {me.name} / {me.my_id}")
    print(f"This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}")
    print(f"This is {type(me.create_email)} call: {me.create_email()}")
    print(f"This is static {type(MyName.say_hello)} with defaults: {me.say_hello()}")
    print(
        f"This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}"
    )
    print(f"Full name: {me.full_name}")
    print(f"Letters in name: {me.count_letters()}")
    me.save_to_file()
    print(f"{" <*> "*20}")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
print("\n--- Відповіді на питання ---")
print(
    "1. Якщо ім'я None — створюється об'єкт з іменем Anonymous, бо так працює метод anonymous_user()."
)
print("2. Текст привітання у say_hello() можна змінити: MyName.say_hello('Hi!')")
print("3. Кількість букв у імені: метод count_letters().")
print(
    f"4. Кількість імен у списку names: {len(names)}. total_names: {MyName.total_names}. Відмінність через створення об'єкта для None."
)
print("5. Конструктор завжди робить ім'я з великої літери.")
print("6. Метод create_email дозволяє змінювати домен через параметр domain.")
print("7. Якщо ім'я містить не лише літери — ValueError.")
print("8. Властивість full_name повертає повну інформацію.")
print("9. Метод save_to_file додає рядок у файл users.txt.")
