"""hello"""
__author__ = "Mohammad Ebraahim"
import pprint as p
import logging


def print_game_status(cnt, pl_1_num, pl_2_num):
    """a"""
    logging.getLogger(__name__).debug("we are in the print_game_status function.")
    p.pprint(f"{cnt}. Guessed Number: {pl_2_num}, " f"Real Number: {pl_1_num}")
