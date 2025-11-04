"""
Core calculator engine.
Registers functions and dispatches calls.
"""
from typing import Callable, Dict

# Global registry: name → (function, arg_count)
_OPERATIONS: Dict[str, tuple[Callable, int]] = {}


def register(name: str, func: Callable, arity: int = 2) -> None:
    """Register a new operation."""
    _OPERATIONS[name.lower()] = (func, arity)


def available_operations() -> list[str]:
    """Return sorted list of operation names."""
    return sorted(_OPERATIONS.keys())


def calculate(op: str, *args) -> float:
    """Execute the requested operation."""
    op = op.lower()
    if op not in _OPERATIONS:
        raise ValueError(f"Unknown operation: {op!r}")

    func, expected = _OPERATIONS[op]
    if len(args) != expected:
        raise ValueError(f"{op!r} expects {expected} argument(s), got {len(args)}")

    return float(func(*args))
