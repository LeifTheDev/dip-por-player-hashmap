from src.player import Player


class PlayerNode:
    """
    A node within a PlayerList. Contains a player along with a __next and __last to allow PlayerList to function as a
    linked list.

    Only intended for use within PlayerList.

    # TODO: Make it easier to access the instance of Player within the node, ideally the users of PlayerList should not
    have to know about PlayerNode to work with its items.
    """

    def __init__(self, player: 'Player' = None, last: 'PlayerNode' = None, next: 'PlayerNode' = None):
        self.__player = player
        self.__last = last
        self.__next = next

    @property
    def next(self):
        """
        The next player in the list. Can only be None or an instance of Player.

        :return:
        """
        return self.__next

    @next.setter
    def next(self, value):
        if not isinstance(value, PlayerNode) and not value is None:
            raise ValueError("PlayerNode.next must be an instance of PlayerNode or None.")
        self.__next = value

    @property
    def last(self):
        """
        The previous player in the list. Can only be None or an instance of Player.

        :return:
        """
        return self.__last

    @last.setter
    def last(self, value):
        if not isinstance(value, PlayerNode) and not value is None:
            raise ValueError("PlayerNode.last must be an instance of PlayerNode or None.")
        self.__last = value

    @property
    def player(self):
        """
        The player contained in this node.

        :return:
        """
        return self.__player

    @property
    def key(self):
        """
        The uid of the stored player.

        :return:
        """
        return self.player.uid

    def __hash__(self):
        return hash(self.player)

    def __str__(self):
        next = self.next.player if self.next else None
        last = self.last.player if self.last else None
        return f"PlayerNode(\n next={next},\n last={last},\n player={self.player}\n)"
