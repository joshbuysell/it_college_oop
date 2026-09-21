import math
from google.adk.agents.llm_agent import Agent


def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2


def calculate_cube_volume(side: float) -> float:
    return side ** 3


def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height


root_agent = Agent(
    model="gemini-2.5-flash",
    name="math_agent",
    description="Виконує математичні обчислення геометричних фігур.",
    instruction=(
        "Ти експертний математичний асистент який допомагає з обчисленнями. "
        "У тебе є інструменти для обчислення площі прямокутника, площі кола, "
        "об'єму куба та площі трикутника. "
        "Використовуй ці інструменти коли потрібно виконати розрахунки. "
        "Відповідай українською мовою та поясни хід обчислень."
    ),
    tools=[
        calculate_rectangle_area,
        calculate_circle_area,
        calculate_cube_volume,
        calculate_triangle_area,
    ],
)
