import pytest
from calculator.parser import parse_expression, evaluate


class TestParseExpression:
    def test_addition(self) -> None:
        assert parse_expression("2 + 3") == (2.0, "+", 3.0)

    def test_no_spaces(self) -> None:
        assert parse_expression("4*5") == (4.0, "*", 5.0)

    def test_negative_left(self) -> None:
        assert parse_expression("-3 + 2") == (-3.0, "+", 2.0)

    def test_floats(self) -> None:
        assert parse_expression("1.5 / 0.5") == (1.5, "/", 0.5)

    def test_power(self) -> None:
        assert parse_expression("2 ** 3") == (2.0, "**", 3.0)

    def test_modulo(self) -> None:
        assert parse_expression("10 % 3") == (10.0, "%", 3.0)

    def test_floor_divide(self) -> None:
        assert parse_expression("7 // 2") == (7.0, "//", 2.0)

    def test_unary_sqrt(self) -> None:
        assert parse_expression("sqrt(9)") == ("sqrt", 9.0)

    def test_unary_fact(self) -> None:
        assert parse_expression("fact(5)") == ("fact", 5.0)

    def test_unary_no_parens(self) -> None:
        assert parse_expression("sqrt 9") == ("sqrt", 9.0)

    def test_malformed(self) -> None:
        with pytest.raises(ValueError, match="Malformed expression"):
            parse_expression("hello")

    def test_empty(self) -> None:
        with pytest.raises(ValueError, match="Malformed expression"):
            parse_expression("")


class TestEvaluate:
    def test_add(self) -> None:
        assert evaluate("2 + 3") == 5.0

    def test_subtract(self) -> None:
        assert evaluate("10 - 4") == 6.0

    def test_multiply(self) -> None:
        assert evaluate("3 * 7") == 21.0

    def test_divide(self) -> None:
        assert evaluate("8 / 2") == 4.0

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            evaluate("5 / 0")

    def test_power(self) -> None:
        assert evaluate("2 ** 10") == 1024.0

    def test_modulo(self) -> None:
        assert evaluate("10 % 3") == 1.0

    def test_floor_divide(self) -> None:
        assert evaluate("7 // 2") == 3.0

    def test_sqrt(self) -> None:
        assert evaluate("sqrt(16)") == 4.0

    def test_factorial(self) -> None:
        assert evaluate("fact(6)") == 720.0
