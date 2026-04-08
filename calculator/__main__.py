"""Entry point — the only module that does I/O."""

from calculator.parser import evaluate


def main() -> None:
    print("Calculator — type an expression (e.g. 2 + 3) or 'quit' to exit.")
    while True:
        try:
            expr = input("> ")
        except EOFError, KeyboardInterrupt:
            print()
            break
        if expr.strip().lower() in ("quit", "exit", "q"):
            break
        try:
            result = evaluate(expr)
            print(f"= {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
