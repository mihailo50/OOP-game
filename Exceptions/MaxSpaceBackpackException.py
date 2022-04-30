

class BackpackSpaceReachedException(Exception):

    def __init__(self):
        super().__init__("Nemate dovoljno mesta u rancu.")