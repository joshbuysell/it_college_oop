"""
demo.py — Демонстрація роботи OOP-класів та інструменту агента
без необхідності API-ключа.
"""

from agent import (
    Rectangle,
    Triangle,
    Circle,
    ShapeStorage,
    calculate_shape_area,
)

print("=" * 58)
print("  Демонстрація роботи геометричного агента (Варіант 2)")
print("=" * 58)

# ── [1] Пряме використання OOP-ієрархії ──────────────────
print("\n[1] Пряме використання OOP-ієрархії:")
shapes = [
    ("Прямокутник (5×3)", Rectangle(5, 3)),
    ("Трикутник (3,4,5)", Triangle(3, 4, 5)),
    ("Коло (r=7)",        Circle(7)),
]
for name, fig in shapes:
    print(f"  {name:22} | площа={fig.area():>10} | периметр={fig.perimeter():>10}")

# ── [2] ShapeStorage — total_area ─────────────────────────
print("\n[2] ShapeStorage — total_area (поліморфізм):")
storage = ShapeStorage()
storage.add(Rectangle(4, 6))
storage.add(Triangle(5, 12, 13))
storage.add(Circle(3))
print(f"  Загальна площа трьох фігур: {storage.total_area()}")

# ── [3] Виклик tool calculate_shape_area ─────────────────
print("\n[3] Виклик tool calculate_shape_area() (як ADK-агент):")
calls = [
    ("rectangle", {"width": 10, "height": 4}),
    ("triangle",  {"a": 6, "b": 8, "c": 10}),
    ("circle",    {"radius": 5}),
]
for shape, params in calls:
    result = calculate_shape_area(shape, params)
    print(f"  {shape:12} params={params}")
    print(f"             → площа={result['area']}, периметр={result['perimeter']}")

# ── [4] Інкапсуляція ──────────────────────────────────────
print("\n[4] Інкапсуляція — спроба доступу до __shapes:")
st = ShapeStorage()
st.add(Circle(2))
try:
    _ = st.__shapes
    print("  ПОМИЛКА: атрибут доступний ззовні!")
except AttributeError:
    print("  OK: атрибут '__shapes' недоступний ззовні (name mangling)")

print("\n" + "=" * 58)
print("  Всі перевірки пройдено успішно!")
print("=" * 58)
