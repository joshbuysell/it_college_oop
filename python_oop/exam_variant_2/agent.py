import math
from abc import ABC, abstractmethod

try:
    from google.adk.agents.llm_agent import Agent
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return round(self.width * self.height, 4)

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 4)


class Triangle(Shape):

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

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(math.pi * self.radius ** 2, 4)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 4)


class ShapeStorage:

    def __init__(self):
        self.__shapes: list[Shape] = []

    def add(self, shape: Shape) -> None:
        self.__shapes.append(shape)

    def total_area(self) -> float:
        return round(sum(s.area() for s in self.__shapes), 4)


def calculate_shape_area(shape: str, params: dict) -> dict:
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
        "area": fig.area(),
        "perimeter": fig.perimeter(),
    }


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
