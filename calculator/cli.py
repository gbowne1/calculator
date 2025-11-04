"""
Command-line interface.
"""
import sys
from .core import calculate, available_operations


def _print_help() -> None:
    ops = ", ".join(available_operations())
    print("Simple calculator")
    print(f"Available operations: {ops}")
    print("Usage: <operation> <arg1> [arg2]")
    print("Example: + 5 3")
    print("Type 'help' for this message, 'quit' to exit.")


def _repl() -> None:
    print("=== Calculator REPL ===")
    _print_help()
    while True:
        try:
            line = input("\n> ").strip()
        except EOFError:
            print("\nBye!")
            break

        if not line:
            continue
        if line.lower() in {"quit", "exit"}:
            print("Bye!")
            break
        if line.lower() == "help":
            _print_help()
            continue

        parts = line.split()
        op = parts[0]
        try:
            args = [float(x) for x in parts[1:]]
        except ValueError:
            print("Error: all arguments must be numbers")
            continue

        try:
            result = calculate(op, *args)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        _repl()
        return 0

    # One-shot mode: calculator.py + 2 3
    if len(argv) < 2:
        print("Usage: run_calculator.py <op> <arg1> [<arg2>...]")
        return 1

    op = argv[0]
    try:
        args = [float(x) for x in argv[1:]]
    except ValueError:
        print("All arguments after the operation must be numbers")
        return 1

    try:
        result = calculate(op, *args)
        print(result)
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
