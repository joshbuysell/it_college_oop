from typing import Final


class Figure:
    FIGURES: Final = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type: str, length: int):
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> int:
        return self.length

    def get_angles(self) -> int:
        angles = {
            "квадрат": 4,
            "прямокутник": 4,
            "трикутник": 3,
        }
        return angles[self.type]


def count_vowels(text: str) -> int:
    vowels = set("аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU")
    return sum(character in vowels for character in text)


def create_name(name: str) -> str:
    if not name.strip():
        raise ValueError("Ім'я не може бути порожнім")
    return name.strip()


def read_positive_number() -> float:
    value = float(input("Введіть додатне число: "))
    if value <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return value
