# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
def func():
    a = ["hello", "hi", "how", "oh"]

    # for i in range(len(a)):
    #     print(f"{i}: {a[i]}")

    for idx, item in enumerate(a):
        print(f"{idx}: {item}")


if __name__ == "__main__":
    func()
