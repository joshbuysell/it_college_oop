"""
Варіант 2 — Агент розрахунку геометричних фігур
Демонструє всі 4 парадигми ООП: абстракція, наслідування, поліморфізм, інкапсуляція
"""

import math
from abc import ABC, abstractmethod

try:
    from google.adk.agents.llm_agent import Agent
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False


# ──────────────────────────────────────────────
# 1. АБСТРАКЦІЯ — абстрактний базовий клас Shape
# ──────────────────────────────────────────────
class Shape(ABC):
    """Абстрактний клас геометричної фігури."""

    @abstractmethod
    def area(self) -> float:
        """Обчислити площу фігури."""

    @abstractmethod
    def perimeter(self) -> float:
        """Обчислити периметр фігури."""


# ──────────────────────────────────────────────
# 2. НАСЛІДУВАННЯ — конкретні фігури
# ──────────────────────────────────────────────
class Rectangle(Shape):
    """Прямокутник."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return round(self.width * self.height, 4)

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 4)


class Triangle(Shape):
    """Трикутник (три сторони — формула Герона)."""

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), 4)

    def perimeter(self) -> float:
        return round(self.a + self.b + self.c, 4)


class Circle(Shape):
    """Коло."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(math.pi * self.radius ** 2, 4)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 4)


# ──────────────────────────────────────────────
# 3. ІНКАПСУЛЯЦІЯ + ПОЛІМОРФІЗМ — ShapeStorage
# ──────────────────────────────────────────────
class ShapeStorage:
    """Сховище геометричних фігур."""

    def __init__(self):
        self.__shapes: list[Shape] = []   # приватний список (інкапсуляція)

    def add(self, shape: Shape) -> None:
        """Додати фігуру до сховища."""
        self.__shapes.append(shape)

    def total_area(self) -> float:
        """
        Повернути суму площ усіх фігур.
        Поліморфізм: кожна фігура викликає свій area().
        """
        return round(sum(s.area() for s in self.__shapes), 4)   # поліморфізм


# ──────────────────────────────────────────────
# Tool для AI-агента
# ──────────────────────────────────────────────
def calculate_shape_area(shape: str, params: dict) -> dict:
    """
    Інструмент агента: обчислити площу та периметр геометричної фігури.

    Args:
        shape:  Назва фігури: "rectangle", "triangle", "circle"
        params: Параметри фігури:
                  rectangle → {"width": float, "height": float}
                  triangle  → {"a": float, "b": float, "c": float}
                  circle    → {"radius": float}

    Returns:
        Словник {"shape": ..., "area": ..., "perimeter": ...}
    """
    shape_lower = shape.lower().strip()

    if shape_lower == "rectangle":
        fig = Rectangle(width=params["width"], height=params["height"])
    elif shape_lower == "triangle":
        fig = Triangle(a=params["a"], b=params["b"], c=params["c"])
    elif shape_lower == "circle":
        fig = Circle(radius=params["radius"])
    else:
        return {"error": f"Невідома фігура: {shape}"}

    storage = ShapeStorage()
    storage.add(fig)

    return {
        "shape": shape_lower,
        "params": params,
        "area": fig.area(),
        "perimeter": fig.perimeter(),
        "total_area_in_storage": storage.total_area(),
    }


# ──────────────────────────────────────────────
# Визначення AI-агента (Google ADK)
# ──────────────────────────────────────────────
if ADK_AVAILABLE:
    root_agent = Agent(
        model="gemini-2.5-flash",
        name="geometry_agent",
        description="Математичний асистент з геометрії.",
        instruction=(
            "Ти математичний асистент з геометрії. "
            "Ти обчислюєш площі та периметри геометричних фігур за введеними розмірами "
            "та пояснюєш формули, які використовуються для розрахунку. "
            "Використовуй функцію 'calculate_shape_area' для обчислень. "
            "Підтримувані фігури: прямокутник (rectangle), трикутник (triangle), коло (circle). "
            "Відповідай виключно українською мовою, будь точним і зрозумілим."
        ),
        tools=[calculate_shape_area],
    )
