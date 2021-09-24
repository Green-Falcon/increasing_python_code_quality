"""a"""
__author__ = "Mohammad Ebraahim"

import random
from player import Player
from utility import print_game_status
import logging
import logging.config

# config
logging.config.fileConfig(disable_existing_loggers=False,
                          fname="logging.ini")
# end of config


class PlayGame(object):
    status = ["progress", "won", "lost"]
    lim_nums = [1, 101]

    def __init__(self, player1, player2):
        self.logger = logging.getLogger(__name__)

        self.logger.debug("Initialising the instance variables. [PlayerGame class]")

        self.player_1 = player1
        self.player_2 = player2
        self.tmp = 20
        self.player_1.status = PlayGame.status[0]
        self.player_2.status = PlayGame.status[0]
        self.player_1.selected_number = random.choice(
            range(PlayGame.lim_nums[0], PlayGame.lim_nums[1])
        )

        self.logger.debug("End of initialising.")

    def start(self, number_of_tries=10):

        self.logger.debug("start method is called.")

        counter = 0
        found_flag = False
        up_lim = PlayGame.lim_nums[1]
        bot_lim = PlayGame.lim_nums[0]
        self.player_2.selected_number = random.choice(range(bot_lim, up_lim))

        self.logger.debug(f"The first guessed number is: {self.player_2.selected_number}. "
                          f"The considered number is: {self.player_1.selected_number}")

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

            self.logger.debug(f"The {counter+1} guessed number is: {self.player_2.selected_number}. "
                              f"The considered number is: {self.player_1.selected_number}")

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

        self.logger.debug(f"The game is finished with '{self.player_2.status}' "
                          f"status for the guessing player. ")


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.debug("Program starts")
    random.seed()
    game = PlayGame(Player("player one", None), Player("player two", None))
    game.start(10)
    Player("Ali", 5)
    logger.debug("Program ends")

