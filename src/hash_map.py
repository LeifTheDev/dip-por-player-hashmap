from src.player_list import PlayerList
from src.player import Player

from typing import Any



class HashMap:
    # TODO: Implement Generics

    def __init__(self):

        self._size: int = 10
        self._length: int = 0

        self._array: list[PlayerList] = [PlayerList() for i in range(self._size)]
        
    @property
    def size(self) -> int:
        """
        The number of PlayerList's in the array used to store players

        :return: int
        """
        return self._size

    def _hash(self, value: str|Player) -> int:
        """
        Hash a player or string using pearson hash

        :param value: str|Player
        :return: int
        """
        if isinstance(value, Player):
            return hash(value) % self._size

        return Player.pearson_hash(value) % self._size

    def add(self, value: Player):
        """
        Add a player to the HashMap

        :param value: Player
        """
        index: int = self._hash(value)
        # TODO: Decide whether to convert the value into a Player
        self._array[index].append(value)
        self._length += 1

    def put(self, key: str, value: Any):
        """
        Update the value with <key> to <value>

        :param key: str
        :param value: Any
        """
        return self.__setitem__(key, value)

    def get(self, key: str) -> Player:
        """
        Return the player at position <key>

        :param key: str

        :return Player:
        """
        return self.__getitem__(key)

    def remove(self, key: str):
        """
        Remove the player at position <key>

        :param key: str
        """
        return self.__delitem__(key)

    def display(self):
        """
        Print the content of the HashMap
        """
        message = f"{self.__class__.__name__}({', '.join([f'{index}: {player_list}' for index, player_list in enumerate(self._array)])})"
        print(message)

    # Type annotations for the return values are set as any as I have not yet decided whether I want these to return anything
    def __getitem__(self, key: str) -> Any:
        index = self._hash(key)

        for player in self._array[index]:
            if player.uid == key:
                return player

        raise KeyError(key)

    def __setitem__(self, key: str, value: Any) -> Any:
        index = self._hash(key)
        self._array[index].update(key, value)

    def __delitem__(self, key: str) -> Any:
        index: int = self._hash(key)
        self._array[index].remove(key)
        self._length -= 1

    def __len__(self) -> int:
        return self._length

    def __iter__(self):
        for linked_list in self._array:
            for node in linked_list:
                yield node.player

    def __repr__(self):
        key_value_map = []
        for linked_list in self._array:
            if not len(linked_list) == 0:
                key_value_map.append(', '.join([f"{repr(player.uid)}: {player.name}" for player in linked_list]))

        return f"{self.__class__.__name__}({', '.join(key_value_map)})"


if __name__ == '__main__':

    hm = HashMap()

    for i in range(13):
        player = Player(i, 'Jane Doe')
        hm.add(player)
    for i in range(13):
        print(i, hm[i])

    for i in "Hello":
        player = Player(i, "John Doe")
        hm.add(player)

    for i in "Hello":
        print(i, hm[i])

    hm.display()
