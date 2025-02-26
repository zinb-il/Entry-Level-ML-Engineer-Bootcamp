from datetime import datetime

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)


def main():
    try:
        d = datetime.strptime("".join([str(i) for i in kata]), '%Y%m%d%H%M')
        print(f"{d.strftime('%m/%d/%Y %H:%M')}")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
