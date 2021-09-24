"""b"""
import random

from human import Human
from typing import List
from typing import Tuple


class TennisPlayer:
    def __init__(self, player: Human, rank: int, score: int):
        self.player: Human = player
        self.rank: int = rank
        self.score: int = score
        self.list_of_honour: List[str] = []
        self.previous_ranks: List[int] = []

    def score_update(self, added_score: int) -> int:
        self.score += added_score
        return self.score

    def rank_update(self, new_rank: int) -> int:
        self.rank = new_rank
        return self.rank

    @property
    def status(self) -> Tuple[str, int, int]:
        return self.player.name, self.rank, self.score

    @property
    def guess_for_future(self) -> Tuple[Tuple[int, int], Human]:
        added_score: int = random.choice(range(1, 100))
        new_rank: int = random.choice(range(1, 1000))
        return (added_score, new_rank), self.player

    @property
    def guess_for_future_v2(self) -> Tuple[Tuple[int, int], Human]:
        added_score: int
        new_rank: int
        added_score = random.choice(range(1, 100))
        new_rank = random.choice(range(1, 1000))
        return (added_score, new_rank), self.player

    @property
    def guess_for_future_v0(self) -> Tuple[Tuple[int, int], Human]:
        added_score = random.choice(range(1, 100))
        new_rank: int = random.choice(range(1, 1000))
        return (added_score, new_rank), self.player

    @property
    def is_good_tennis_player(self) -> bool:
        if self.rank < 5:
            return True
        else:
            return False
