"""a"""
__author__ = "Mohammad Ebraahim"

import logging


class Player:
    """a"""

    def __init__(self, name, selected_number, status=None):
        self.logger = logging.getLogger(__name__)

        self.logger.debug("we are in the __init__ of Player class.")

        self.selected_number = selected_number
        self._status = status
        self._name = name

        self.logger.debug("end of __init__ of Player class.")


    @property
    def status(self):
        """a"""
        self.logger.debug("We are in status property (get).")
        return self._status

    @status.setter
    def status(self, val):
        """a"""
        self.logger.debug("We are in status property (set).")
        self._status = val

    def __str__(self):
        """a"""
        self.logger.debug("We are in __str__ function of game.")
        return f"{self._name} is {self.status}"

    def my_player_name(self):
        """a"""
        self.logger.debug("We are in my_player_name")
        return f"{self._name} {self.selected_number}"
