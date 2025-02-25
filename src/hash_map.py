from player_list import PlayerList

from typing import Any

class HashMap:
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

    def _hash(self, value: Any) -> int:
        ...

    def put(self, key: str, value: Any) -> Any:
        return self.__setitem__(key, value)

    def get(self, key: str) -> Any:
        return self.__getitem__(key)

    def remove(self, key: str) -> Any:
        return self.__delitem__(key)

    def __getitem__(self, item: Any) -> Any:
        ...

    def __setitem__(self, key: str, value: Any) -> Any:
        ...

    def __delitem__(self, key: str) -> Any:
        ...

    def __len__(self) -> int:
        ...