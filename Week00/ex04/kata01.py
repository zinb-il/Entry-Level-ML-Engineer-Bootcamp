# Put this at the top of your kata01.py file
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }


def main():
    try:
        for indx, val in kata.items():
            print(f"{indx} was created by {val}")
    except Exception as err:
        print(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
