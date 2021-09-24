"""
player.py
=========

Here, the code contains the :class:`Player` class or :class:`~game.player.Player`
that is demanded for our game.

:meth:`my_player_name` method or :meth:`~Player.my_player_name` method?

:func:`~game.utility.print_game_status`?

"""

__author__ = "Mohammad Ebraahim"


class Player:
    """
    The players of the game should be instantiated with this class.
    The :meth:`my_player_name` (or :meth:`Player.my_player_name`) method is here.


    :ivar str _name: keeps the name of the player.
    :ivar int selected_number: will keep the chosen number even guessed or kept to be guessed combine combine
                               keep the chosen number even guessed or kept to be guessed.

    """
    def __init__(self, name, selected_number, status=None):
        """
        The ``__init__`` method is here for initialization.

        :param str name: The name of player.
        :param int selected_number: The selected or guessed number.
        :param str status: The game status of the player.
        """
        self.selected_number = selected_number
        self._status = status
        self._name = name

    @property
    def status(self):
        """
        This is used to show the status of the player.

        :ivar a: This is a simple variable.
        :ivar b: This is variable that is not going to be used.

        :return: The :attr:`status` will return ``_status``.
        """
        a = 10
        b = a
        return self._status

    @status.setter
    def status(self, val):
        self._status = val

    def __str__(self):
        return f"{self._name} is {self.status}"

    def my_player_name(self):
        """
        This will try to output the value of :attr:`status`.

        :return: :attr:`_name` alongside :attr:`selected_number`.
        """
        return f"{self._name} {self.selected_number}"


if __name__ == "__main__":
    a = 10
    b = 100
    print(a + b)

