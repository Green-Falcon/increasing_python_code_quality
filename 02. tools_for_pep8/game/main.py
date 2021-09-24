__author__ = "Mohammad Ebraahim"

import random
import numbers
from player import Player
from utility import print_game_status

temp_mod = __import__("New Text Document")

temp = (
    "aaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb cccccccccccc"
    "cccccccccc eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
)
print(temp, numbers)
a = 10


class Foo:
    def __init__(self):
        self.a = 1
        self.b = 2

    def set(self, in_a, in_b=10):
        self.a = in_a
        self.b = in_b
        # raise "hello"


class PlayGame(object):
    status = ["progress", "won", "lost"]
    lim_nums = [1, 101]

    def __init__(self, player1, player2):
        self.player_1 = player1
        self.player_2 = player2
        self.tmp = 20
        self.player_1.status = PlayGame.status[0]
        self.player_2.status = PlayGame.status[0]
        self.player_1.selected_number = random.choice(
            range(PlayGame.lim_nums[0], PlayGame.lim_nums[1])
        )

    def start(self, number_of_tries=10):
        counter = 0
        found_flag = False
        up_lim = PlayGame.lim_nums[1]
        bot_lim = PlayGame.lim_nums[0]
        self.player_2.selected_number = random.choice(range(bot_lim, up_lim))

        while counter < number_of_tries:
            counter += 1
            print_game_status(
                counter,
                self.player_1.selected_number,
                self.player_2.selected_number,
            )
            if self.player_2.selected_number == self.player_1.selected_number:
                found_flag = True
                break
            elif self.player_2.selected_number > self.player_1.selected_number:
                up_lim = self.player_2.selected_number
            else:
                # self.player_2.selected_number < self.player_1.selected_number
                bot_lim = self.player_2.selected_number + 1

            self.player_2.selected_number = random.choice(
                range(bot_lim, up_lim)
            )

        self.player_2.status = (
            PlayGame.status[1] if found_flag else PlayGame.status[-1]
        )
        self.player_1.status = (
            PlayGame.status[1] if not found_flag else PlayGame.status[-1]
        )
        print(
            f"The game is finished with '{self.player_2.status}' "
            f"status for the guessing player. "
        )


if __name__ == "__main__":
    random.seed()
    game = PlayGame(Player("player one", None), Player("player two", None))
    game.start(10)
    Player("Ali", 5)
    Foo().set(in_b=10, in_a=20)
    temp_mod.func()

    a = 20 + 10
    b = [1, 2, 3, 4, 5]  # hello
