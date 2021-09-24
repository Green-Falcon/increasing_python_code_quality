"""hello"""
__author__ = "Mohammad Ebraahim"
import pprint as p


def print_game_status(cnt, pl_1_num, pl_2_num):
    """a"""
    p.pprint(f"{cnt}. Guessed Number: {pl_2_num}, " f"Real Number: {pl_1_num}")


if __name__ == "__main__":
    import this