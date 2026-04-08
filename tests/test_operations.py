import pytest
from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    floor_divide,
    square_root,
    factorial,
)


class TestAdd:
    def test_positive(self) -> None:
        assert add(2, 3) == 5

    def test_negative(self) -> None:
        assert add(-1, -1) == -2

    def test_floats(self) -> None:
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero(self) -> None:
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive(self) -> None:
        assert subtract(5, 3) == 2

    def test_negative_result(self) -> None:
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_positive(self) -> None:
        assert multiply(4, 3) == 12

    def test_by_zero(self) -> None:
        assert multiply(5, 0) == 0


class TestDivide:
    def test_positive(self) -> None:
        assert divide(10, 2) == 5.0

    def test_float_result(self) -> None:
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)


class TestPower:
    def test_square(self) -> None:
        assert power(3, 2) == 9

    def test_zero_exponent(self) -> None:
        assert power(5, 0) == 1

    def test_fractional_exponent(self) -> None:
        assert power(4, 0.5) == pytest.approx(2.0)

    def test_negative_exponent(self) -> None:
        assert power(2, -1) == pytest.approx(0.5)


class TestModulo:
    def test_positive(self) -> None:
        assert modulo(10, 3) == 1

    def test_even_division(self) -> None:
        assert modulo(9, 3) == 0

    def test_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            modulo(5, 0)


class TestFloorDivide:
    def test_exact(self) -> None:
        assert floor_divide(10, 2) == 5

    def test_truncates(self) -> None:
        assert floor_divide(7, 2) == 3

    def test_negative(self) -> None:
        assert floor_divide(-7, 2) == -4

    def test_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot floor divide by zero"):
            floor_divide(5, 0)


class TestSquareRoot:
    def test_perfect(self) -> None:
        assert square_root(9) == 3.0

    def test_zero(self) -> None:
        assert square_root(0) == 0.0

    def test_non_perfect(self) -> None:
        assert square_root(2) == pytest.approx(1.4142135623730951)

    def test_negative(self) -> None:
        with pytest.raises(ValueError, match="Cannot take square root of a negative"):
            square_root(-1)


class TestFactorial:
    def test_zero(self) -> None:
        assert factorial(0) == 1.0

    def test_five(self) -> None:
        assert factorial(5) == 120.0

    def test_one(self) -> None:
        assert factorial(1) == 1.0

    def test_negative(self) -> None:
        with pytest.raises(ValueError, match="non-negative integer"):
            factorial(-1)

    def test_non_integer(self) -> None:
        with pytest.raises(ValueError, match="non-negative integer"):
            factorial(3.5)
