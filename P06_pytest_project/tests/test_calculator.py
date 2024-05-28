from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        # arrage
        a = 9999
        b = 8888
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 1111
        assert result == expected

    def test_multiply(self):
        # arrage
        a = 1111
        b = 2222
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 2468642
        assert result == expected

    def test_divide(self):  
        # arrange
        a = 1000
        b = 5
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 200
        assert result == expected

    def test_divide_by_zero(self):  
        # arrange
        a = 1000
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)