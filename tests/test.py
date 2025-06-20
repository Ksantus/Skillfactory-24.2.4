import pytest

from app.calculator import Calculator


class TestCale:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 24, 15) == 9

    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 7) == 28

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3

    def teardown(self):
        print("Выполнение метода Teardown")
