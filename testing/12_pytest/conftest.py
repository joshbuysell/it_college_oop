import pytest

from app import Figure


@pytest.fixture
def square() -> Figure:
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def allowed_figures() -> tuple[str, ...]:
    return Figure.FIGURES