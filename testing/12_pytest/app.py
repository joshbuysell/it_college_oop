from typing import Final


class Figure:
    FIGURES: Final = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type: str, length: int):
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    def get_angles(self) -> int:
        angles = {
            "квадрат": 4,
            "прямокутник": 4,
            "трикутник": 3,
        }
        return angles[self.type]