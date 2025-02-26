import sys
from typing import List


def reverse_str(argv: List[str]) -> None:
    """This function reverses a list of strings and swaps
the case of their letters.
        Args:
            argv : Liste of string to reverse
    """
    try:
        if not argv:
            return
        strings = [i.swapcase()[::-1] for i in argv][::-1]
        print(" ".join(strings))
    except Exception as err:
        print(f"ExceptionError : {err}")


def main(argv: List):
    try:
        reverse_str(argv)
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main(sys.argv[1:])
