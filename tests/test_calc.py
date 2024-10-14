import pytest
from mypackage.lib.calc import Calculator

class TestCalculator:
    @pytest.mark.parametrize("x1,x2,expected", [
        (1,2, 3),
        (1,4, 5),
        (1,5, 9)
    ])
    def test_calc_sum(self, x1,x2,expected):
        calc = Calculator()
        assert(calc.calc_sum(x1,x2))==expected, "wrong answer"
    