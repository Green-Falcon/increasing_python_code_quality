"""a"""

from typing import (
    Dict,
    Union,
)


class CriticizedMovie:
    stars: int
    movie_name: str
    director: str
    year: int

    movie_rates: Dict[str, int] = \
        {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

    def __init__(self, mn: str, s: Union[str, int], d: str, y: int):
        self.movie_name = mn
        self.director = d
        self.year = y

        if type(s) is int:
            self.stars = s
        elif type(s) is str:
            self.stars = self.movie_rates[s]
        else:
            raise Exception("Type of s should be valid str or int")

    def __str__(self) -> str:
        return f"'{self.movie_name}' has rate {self.stars}."


if __name__ == "__main__":
    movie = CriticizedMovie("A Movie", 5, "Mr. B", 1950)
    print(movie)
