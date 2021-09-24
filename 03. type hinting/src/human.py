"""a"""


class Human:
    def __init__(self, name: str, age: int, height: int):
        self.name: str = name
        self.age: int = age
        self.height: int = height

    def __str__(self) -> str:
        return f"{self.name.title()} is {self.age} and has" \
               f" {self.height}cm height."


if __name__ == "__main__":
    from tennis import TennisPlayer

    ali = Human("Ali", 25, 180)
    ahmad = Human("Ahmad", 27, 185)
    ali_p = TennisPlayer(ali, 25, 7000)
    ahmad_p = TennisPlayer(ahmad, 27, 7200)
    print(ali)
    print(ahmad)
    t = ali_p.guess_for_future_v0
    print(t[0], t[1])
