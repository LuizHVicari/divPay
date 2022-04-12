from user import User


class Purchase:
    def __init__(self, value : int, owner : User):
        self.value = value
        self.owner = owner
