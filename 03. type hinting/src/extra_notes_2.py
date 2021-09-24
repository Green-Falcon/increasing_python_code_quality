"""a"""

from typing import (
    Iterable,
    List,
    Optional
)


def show_items(seq: Iterable):
    for item in seq:
        print(item, end=", ")
    print()


# show_items([1, 2, 3, 4, 5])
# show_items(["hello", "hi", "how"])
# show_items({1, 2, 3, 4, 5, 7, 8, 1})
# show_items("hello")
# show_items({1: 2, 2: 3, 4: 5})
# show_items(range(8))


# Union[None, x]  == Optional[x]
# Optional[List[int]]  == Union[None, List[int]]
# Union[int, float, set, None] xxxxx Optional[int, float, set]

def make_new_list(inp: Optional[List[int]], inp_2: Optional[int] = None) -> List[int]:
    list_mine: List[int]
    if inp is None:
        list_mine = []
    elif type(inp) is list:
        list_mine = []
        for item in inp:
            list_mine.append(item)
    else:
        raise Exception("...")

    list_mine.append(inp_2)

    return list_mine


a = [1, 2, 3, 4, 5]
b = make_new_list(a)
print(b)
