import sys
from typing import List


def main(argv: List):
    try:
        if (len(sys.argv) < 2):
            sys.exit(0)
        assert len(sys.argv) == 2, "more than one argument is provided"
        n = int(argv[1])
        if not n:
            print("I'm Zero.")
        else:
            print("I'm Odd." if n % 2 else "I'm Even.")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main(sys.argv)
