from src.player import Player
from src.player_node import PlayerNode


class PlayerList:
    """
    A two-way linked list intended for storing instances of Player.

    # TODO (optional): Add a random access to make using the list more convenient. Not required by assessment.
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        """
        The head or 'start' of the list.

        :return:
        """
        return self.__head

    @property
    def tail(self):
        """
        The tail or 'end' of the list.

        :return:
        """
        return self.__tail

    @property
    def is_empty(self):
        """
        True if the list is empty, False if it is populated.

        :return:
        """
        return self.__tail is None and self.__head is None

    def append(self, player: Player):
        """
        Add a player to the end of the list.

        :param player:
        :return:
        """
        if not isinstance(player, Player):
            print(isinstance(player, Player))
            print(type(player))
            raise ValueError("PlayerList can only hold instances of Player")

        node = PlayerNode(player)

        if self.is_empty:
            self.__head = node
            self.__tail = node
            return

        if self.__tail is self.__head:
            self.__tail = node
            self.__head.next = self.__tail
            self.__tail.last = self.__head
            return

        node.last = self.__tail
        self.__tail.next = node
        self.__tail = node

    def prepend(self, player: Player):
        """
        Add a player to the start of the list.
        .

        :param player:
        :return:
        """
        if not isinstance(player, Player):
            raise ValueError("PlayerList can only hold instances of PlayerNode")

        node = PlayerNode(player=player)

        if self.is_empty:
            self.__tail = node
            self.__head = node
            return

        if self.__tail is self.__head:
            self.__tail = self.__head
            self.__tail.last = node
            self.__head = node
            self.__head.next = self.__tail
            return

        node.next = self.__head
        self.__head.last = node
        self.__head = node

    def remove_at_head(self):
        """
        Remove the player at the head (start) of the list.

        :return:
        """
        if not self.__head.next:
            self.__head = None
            self.__tail = None
            return

        self.__head = self.__head.next
        self.__head.last = None

    def remove_at_tail(self):
        """
        Remove the player at the tail (end) of the list.

        :return:
        """
        if not self.__tail.last:
            self.__head = None
            self.__tail = None
            return

        self.__tail = self.__tail.last
        self.__tail.next = None

    def remove(self, key: str) -> Player:
        """
        Remove a player from the list by its key. This key matches the uid of the node's player.

        :param key: The key to remove.
        :return:
        """
        # TODO (optional): Add an algorithm to make the key-search look from both __head and __tail if it is more
        #  efficient to do so, or add an argument to toggle this.

        if self.is_empty:
            raise KeyError(f"Key '{key}' not found")

        current = self.__head

        while current.next:
            if current.key == key:
                if current == self.head:
                    self.remove_at_head()
                    return current.player

                current.last.next = current.next
                current.next.last = current.last
                return current.player

            current = current.next

        # Extra check since the loop will exit before checking self.__tail
        if self.__tail.key == key:
            self.remove_at_tail()
            return current.player

        raise KeyError(f"Key '{key}' not found")

    def update(self, key: str, value: str):
        self.__setitem__(key, value)

    def display(self, forward: bool = True):
        """
        Print all the nodes in the list.

        :param forward: Whether to print head -> tail or tail -> head.
        :return:
        """
        nodes = [str(node) for node in self]

        if forward:
            print(f"PlayerList(\n {',\n '.join(nodes)})")
            return

        print(f"PlayerList(\n {',\n '.join(reversed(nodes))})")

    def check_health(self) -> bool:
        """
        Check if both __head and __tail point towards each other. Exists mostly for debugging purposes, this scenario
        should never occur unintentionally unless there is a bug in the code.

        :return: bool - True if __head and __tail point towards each other. False is they do not.
        """
        raise NotImplementedError("This method has not been implemented.")

    def __len__(self):
        return len([i for i in self])

    def __iter__(self):
        if self.is_empty:
            return
        current = self.head
        while current.next:
            yield current.player
            current = current.next
        yield current.player

    def __contains__(self, item):
        for player in self:
            if player == item:
                return True

        return False

    def __setitem__(self, key, value):
        for player in self:
            if player.uid == key:
                player.name = value
                return
        raise KeyError(key)

    def __repr__(self):
        nodes = [str(node) for node in self]
        return f"PlayerList(\n {',\n '.join(nodes)})"
