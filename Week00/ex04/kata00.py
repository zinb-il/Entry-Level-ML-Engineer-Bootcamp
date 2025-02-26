# Put this at the top of your kata00.py file
kata = (19, 42, 21)


def main():
    try:
        ls = [str(i) for i in kata]
        print(f"The {len(kata)} numbers are: {', '.join(ls)}")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
