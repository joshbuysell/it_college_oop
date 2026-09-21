import unittest
from unittest.mock import patch

from app import Figure, count_vowels, create_name, read_positive_number


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.figure_types = ("квадрат", "прямокутник", "трикутник")

    @classmethod
    def tearDownClass(cls):
        cls.figure_types = None

    def setUp(self):
        self.figure = Figure("квадрат", 5)

    def tearDown(self):
        self.figure = None

    def test_figure_type(self):
        self.assertEqual("квадрат", self.figure.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.figure.get_figure_length)

    def test_figure_types_with_subtests(self):
        for figure_type in self.figure_types:
            with self.subTest(figure_type=figure_type):
                self.assertEqual(figure_type, Figure(figure_type, 5).get_figure_type)

    def test_figure_angles(self):
        expected_angles = {
            "квадрат": 4,
            "прямокутник": 4,
            "трикутник": 3,
        }
        for figure_type, angles in expected_angles.items():
            with self.subTest(figure_type=figure_type):
                self.assertEqual(angles, Figure(figure_type, 5).get_angles())

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_lengths(self):
        for length in (0, -1):
            with self.subTest(length=length):
                with self.assertRaises(AssertionError):
                    Figure("квадрат", length)


class TestValidationFunctions(unittest.TestCase):
    def test_count_vowels_in_english_text(self):
        self.assertEqual(5, count_vowels("education"))

    def test_count_vowels_in_empty_text(self):
        self.assertEqual(0, count_vowels(""))

    def test_count_vowels_in_digits(self):
        self.assertEqual(0, count_vowels("12345!?"))

    def test_count_vowels_in_ukrainian_text(self):
        self.assertEqual(4, count_vowels("Україна"))

    def test_create_name(self):
        self.assertEqual("Олена", create_name(" Олена "))

    def test_create_name_rejects_empty_value(self):
        with self.assertRaises(ValueError):
            create_name("   ")

    @patch("builtins.input", return_value="12.5")
    def test_read_positive_number_uses_mocked_input(self, mocked_input):
        self.assertEqual(12.5, read_positive_number())
        mocked_input.assert_called_once_with("Введіть додатне число: ")

    @patch("builtins.input", return_value="0")
    def test_read_positive_number_rejects_non_positive_value(self, mocked_input):
        with self.assertRaises(ValueError):
            read_positive_number()
        mocked_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
