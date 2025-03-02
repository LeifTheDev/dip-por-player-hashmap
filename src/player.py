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
        return hash(self.__uid)

    def __str__(self):
        return f"Player(uuid={self.uid}, name={self.name})"
