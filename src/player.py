import random

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
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

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Player.name must be a string")
        self.__name = value

    @staticmethod
    def pearson_hash(key):
        """
        Apply the pearson hash algorithm to the given key.

        """
        key_bytes = bytes(str(key), encoding="utf-8")

        hash_ = 0
        hash_ = sum([pearson_table[hash_ ^ byte] for byte in key_bytes])

        return hash_

    def __hash__(self):
        return self.pearson_hash(self.__uid)

    def __str__(self):
        return f"Player(uuid={repr(self.uid)}, name={repr(self.name)})"

    def __repr__(self):
        return self.__str__()

