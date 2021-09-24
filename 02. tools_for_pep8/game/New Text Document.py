# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name


def func():
    print("hi")


def func_2():
    print("hello")


def f(b, a_1=None):
    if a_1 is None:
        a_1 = []
    a_1.append(b)
    return a_1


print(f(10, [1]))
print(f(20, [2]))
print(f(7))
print(f(14))
print(f(2))
