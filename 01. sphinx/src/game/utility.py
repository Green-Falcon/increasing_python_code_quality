"""
utility.py
==========

This module contains a kind of printing function to
be utilized throughout the package.

:func:`print_game_status` function is my favorite one.

Go to :attr:`~.main.PlayGame.player_1` is here.

"""

__author__ = "Mohammad Ebraahim"

import pprint as p


def print_game_status(cnt, pl_1_num, pl_2_num):
    """
    :func:`print_game_status` is going to be used to show the game status.

    :param int cnt: The counter used to show the guessed number.
    :param Player pl_1_num: An instance of :class:`~game.main.PlayGame`. Keeps the number in mind.
    :param Player pl_2_num: An instance of :class:`~game.main.PlayGame`. Keeps the number in mind.
    :return: None
    """
    p.pprint(f"{cnt}. Guessed Number: {pl_2_num}, "
             f"Real Number: {pl_1_num}")



