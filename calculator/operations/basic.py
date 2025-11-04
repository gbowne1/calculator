"""
Basic arithmetic: +, −, ×, ÷
"""
from ..core import register


def _add(a: float, b: float) -> float:
    return a + b


def _sub(a: float, b: float) -> float:
    return a - b


def _mul(a: float, b: float) -> float:
    return a * b


def _div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


# Register them
register('+', _add)
register('add', _add)
register('-', _sub)
register('subtract', _sub)
register('*', _mul)
register('multiply', _mul)
register('/', _div)
register('divide', _div)
