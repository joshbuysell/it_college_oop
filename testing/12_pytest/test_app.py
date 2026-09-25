import pytest

from app import Figure


@pytest.mark.unit
def test_triangle_type() -> None:
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


@pytest.mark.unit
def test_square_fixture_properties(square: Figure) -> None:
    assert square.type == "квадрат"
    assert square.length == 10
    assert square.get_angles() == 4


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type: str) -> None:
    figure = Figure(figure_type, 1)
    assert figure.type == figure_type


def test_module_fixture_can_be_used_first(allowed_figures: tuple[str, ...]) -> None:
    assert allowed_figures == Figure.FIGURES


def test_module_fixture_can_be_used_second(allowed_figures: tuple[str, ...]) -> None:
    assert "трикутник" in allowed_figures


@pytest.mark.parametrize("figure_type", ("коло", "овал", "п'ятикутник"))
def test_invalid_figure_type(figure_type: str) -> None:
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 1)


@pytest.mark.parametrize("length", (0, -1, -10))
def test_invalid_length(length: int) -> None:
    with pytest.raises(AssertionError, match="Довжина"):
        Figure("квадрат", length)