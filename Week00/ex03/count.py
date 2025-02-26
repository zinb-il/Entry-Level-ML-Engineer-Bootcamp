import sys
import string as t


def text_analyzer(s: str = None) -> None:
    """ This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    assert isinstance(s, str) or s is None, "argument is not a string"
    if not s:
        s = input("What is the text to analyze?\n")
    print(f"The text contains {len(s)} characters:")
    print(f"- {len([i for i in s if i.isupper()])} upper letter(s)")
    print(f"- {len([i for i in s if i.islower()])} lower letter(s)")
    print(f"- {len([i for i in s if i in t.punctuation])} punctuation mark(s)")
    print(f"- {len([i for i in s if i.isspace()])} space(s)")
    print(f"- {len([i for i in s if i.isdigit()])} digit(s)")


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        s = None
        if len(argv) > 1:
            s = argv[1]
        text_analyzer(s)
    except AssertionError as msg:
        print(f"AssertionError {msg}")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main(sys.argv)
