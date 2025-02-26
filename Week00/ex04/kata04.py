# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)


def main():
    try:
        m = f"module_{str(kata[0]).zfill(2)}"
        e = f"ex_{str(kata[1]).zfill(2)}"
        n1 = f"{kata[2]:0.2f}"
        n2 = f"{kata[3]:.2e}"
        n3 = f"{kata[4]:.2e}"
        print(f"{m}, {e} : {n1}, {n2}, {n3}")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
