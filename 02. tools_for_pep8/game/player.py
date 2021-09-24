"""a"""
__author__ = "Mohammad Ebraahim"


class Player:
    """a"""

    def __init__(self, name, selected_number, status=None):
        self.selected_number = selected_number
        self._status = status
        self._name = name

    @property
    def status(self):
        """a"""
        return self._status

    @status.setter
    def status(self, val):
        """a"""
        self._status = val

    def __str__(self):
        """a"""
        return f"{self._name} is {self.status}"

    def my_player_name(self):
        """a"""
        return f"{self._name} {self.selected_number}"
