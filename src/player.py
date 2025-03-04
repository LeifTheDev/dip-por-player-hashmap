import random

random.seed(42)
pearson_table = list(range(256))
random.shuffle(pearson_table)


class Player:
    """
    Represents a player with a name and uid.

    """

    def __init__(self, uid: str, name: str):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __hash__(self):
        key_bytes = bytes(self.__uid, encoding="utf-8")
        hash_ = 0
        hash_ = [pearson_table[hash_ ^ byte] for byte in key_bytes]

        return hash_

    def __str__(self):
        return f"Player(uuid={repr(self.uid)}, name={repr(self.name)})"
