"""Expression parsing. No I/O."""

import re
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

BINARY_OPERATORS: dict[str, callable] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulo,
    "//": floor_divide,
}

UNARY_FUNCTIONS: dict[str, callable] = {
    "sqrt": square_root,
    "fact": factorial,
}

# Match multi-char operators first (** and //) before single-char ones
_BINARY_RE = re.compile(r"^(-?\d+\.?\d*)\s*(\*\*|//|[+\-*/%])\s*(-?\d+\.?\d*)$")
_UNARY_RE = re.compile(r"^(sqrt|fact)\s*\(?\s*(-?\d+\.?\d*)\s*\)?\s*$")


def parse_expression(expression: str) -> tuple[float, str, float] | tuple[str, float]:
    """Parse a binary or unary expression.

    Binary: 'number operator number' → (left, operator, right)
    Unary:  'func(number)' → (func_name, operand)
    Raises ValueError for malformed input.
    """
    expression = expression.strip()

    unary_match = _UNARY_RE.match(expression)
    if unary_match:
        return unary_match.group(1), float(unary_match.group(2))

    binary_match = _BINARY_RE.match(expression)
    if binary_match:
        return (
            float(binary_match.group(1)),
            binary_match.group(2),
            float(binary_match.group(3)),
        )

    raise ValueError(
        f"Malformed expression: '{expression}'. "
        "Expected 'number op number' or 'sqrt/fact(number)'"
    )


def evaluate(expression: str) -> float:
    """Evaluate an arithmetic expression string."""
    parsed = parse_expression(expression)

    if len(parsed) == 2:
        func_name, operand = parsed
        if func_name not in UNARY_FUNCTIONS:
            raise ValueError(f"Unknown function: '{func_name}'")
        return UNARY_FUNCTIONS[func_name](operand)

    left, operator, right = parsed
    if operator not in BINARY_OPERATORS:
        raise ValueError(f"Unknown operator: '{operator}'")
    return BINARY_OPERATORS[operator](left, right)
