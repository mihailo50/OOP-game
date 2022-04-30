
class NotAllowedWeaponException(Exception):
    def __init__(self):
        super().__init__("Izabrano oruzje nije dozvoljeno za vaseg heroja.")