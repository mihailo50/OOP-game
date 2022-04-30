import random

class Cudoviste(object):

    def __init__(self):
        self.health = 100

    @staticmethod
    def napad(target, attack_type):
        target.health = target.health - attack_type['damage']
        return target.health

    
class Zmaj(Cudoviste):

    @staticmethod
    def generisi_napad():
        attack_types = [
            {'type': 'Udarac', 'damage': 5},
            {'type': 'Vatra', 'damage': 20}
        ]
        attack = random.choice(attack_types)
        return attack


class Pauk(Cudoviste):

    @staticmethod
    def generisi_napad():
        attack_types = [
            {'type': 'Udarac', 'damage': 5},
            {'type': 'Ujed', 'damage': 8}
        ]
        attack = random.choice(attack_types)
        return attack