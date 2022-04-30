

class NoWeaponException(Exception):

    def __init__(self):
        super().__init__('Ranac je prazan.')