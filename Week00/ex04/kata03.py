# Put this at the top of your kata03.py file
kata = "The right format"


def main():
    try:
        b = 0
        if len(kata) < 42:
            b = 42 - len(kata)
        print(f"{'-' * b}{kata[:42]}", end="")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
