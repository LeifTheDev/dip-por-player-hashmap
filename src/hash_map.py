from src.player_list import PlayerList
from src.player_node import PlayerNode
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
        return self._size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("HashMap.size must be an int.")
        self._size = value

    def _hash(self, value: str) -> int:
        # TODO: Implement *custom* hash algorithm
        return hash(value) % self._size

    def add(self, value: Player):
        index: int = self._hash(value.uid)
        # TODO: Decide whether to convert the value into a Player
        self._array[index].append(value)
        self._length += 1

    def put(self, key: str, value: Any) -> Any:
        return self.__setitem__(key, value)

    def get(self, key: str) -> Any:
        return self.__getitem__(key)

    def remove(self, key: str) -> Any:
        return self.__delitem__(key)

    # Type annotations for the return values are set as any as I have not yet decided whether I want these to return anything
    def __getitem__(self, key: str) -> Any:
        index = self._hash(key)

        for item in self._array[index]:
            if item.key == key:
                return item.player

    def __setitem__(self, key: str, value: Any) -> Any:
        index = self._hash(key)
        # TODO: Consider adding update() method to PlayerList
        self._array[index].remove(key)
        self._array[index].prepend(value)

        item: PlayerNode
        for item in self._array[index]:
            item.player.name = "Hi"

    def __delitem__(self, key: str) -> Any:
        index: int = self._hash(key)
        self._array[index].remove(key)
        self._length -= 1

    def __len__(self) -> int:
        return self._length

    def __repr__(self):
        key_value_map = []
        for linked_list in self._array:
            if not len(linked_list) == 0:
                key_value_map.append(', '.join([f"{repr(node.key)}: {node.player}" for node in linked_list]))

        return f"{self.__class__.__name__}({', '.join(key_value_map)})"
