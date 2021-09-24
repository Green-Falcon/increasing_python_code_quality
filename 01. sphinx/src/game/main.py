"""
main.py
=======

I want to have a link the the :meth:`.start` method.

"""

__author__ = "Mohammad Ebraahim"

import random
from player import Player
from utility import print_game_status


class Foo:
    """
    Simple class name :class:`Foo`.

    :ivar a: first variable
    :ivar b: second variable
    """
    def __init__(self):
        self.a = 1
        self.b = 2

    def set(self, in_a, in_b):
        """
        lorem lorem lorem

        :ivar a: first variable
        :ivar b: second variable

        :param in_a: used to be for a
        :param in_b: used to be for b
        :return: None
        """
        self.a = in_a
        self.b = in_b


class PlayGame(object):
    #: :attr:`status` is used here.
    status = ["progress",
              "won",
              "lost"]
    lim_nums = [1, 101]  #: int values in the range [1, 101)

    def __init__(self, player_1, player_2):
        self.player_1 = player_1  #: The :attr:`player_1` instance variable is used here.
        #: :attr:`player_2` is here.
        #: It's a member of :class:`.Player`
        self.player_2 = player_2
        self.tmp = 20
        """
        :attr:`tmp` is defined here, but it is useless. 
        Can you see this?
        """
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
        self.player_2.selected_number = random.choice(
            range(bot_lim, up_lim)
        )

        while counter < number_of_tries:
            counter += 1
            print_game_status(counter,
                              self.player_1.selected_number,
                              self.player_2.selected_number)
            if self.player_2.selected_number == self.player_1.selected_number:
                found_flag = True
                break
            elif self.player_2.selected_number > self.player_1.selected_number:
                up_lim = self.player_2.selected_number
            else:  # self.player_2.selected_number < self.player_1.selected_number
                bot_lim = self.player_2.selected_number + 1

            self.player_2.selected_number = random.choice(
                range(bot_lim, up_lim)
            )

        self.player_2.status = PlayGame.status[1] if found_flag else PlayGame.status[-1]
        self.player_1.status = PlayGame.status[1] if not found_flag else PlayGame.status[-1]
        print(f"The game is finished with '{self.player_2.status}' status for the guessing player. ")


if __name__ == "__main__":
    random.seed()
    game = PlayGame(
        Player("player one", None),
        Player("player two", None)
    )
    game.start(10)
    Player("Ali", 5)
