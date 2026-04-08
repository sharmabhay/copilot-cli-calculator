"""Pure math operations. No I/O, no side effects."""

import math


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    return a**b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def floor_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot floor divide by zero")
    return a // b


def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def factorial(a: float) -> float:
    if a < 0 or a != int(a):
        raise ValueError("Factorial requires a non-negative integer")
    return float(math.factorial(int(a)))
