import first


def show_utility_for_second():
    print("We are in the `second` module.")


if __name__ == "__main__":
    show_utility_for_second()
    # first.show_utility_for_first()
    print(__name__)
    print(first.__name__)
