import pytest

from app import Figure


@pytest.mark.parametrize(
    ("figure_type", "expected_angles"),
    (
        ("квадрат", 4),
        ("прямокутник", 4),
        ("трикутник", 3),
    ),
)
def test_get_angles_for_each_figure(figure_type: str, expected_angles: int) -> None:
    assert Figure(figure_type, 10).get_angles() == expected_angles


@pytest.mark.parametrize("figure_type", ("коло", "овал"))
def test_invalid_figure_type(figure_type: str) -> None:
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 1)


@pytest.mark.parametrize("length", (0, -1))
def test_invalid_length(length: int) -> None:
    with pytest.raises(AssertionError, match="Довжина"):
        Figure("квадрат", length)