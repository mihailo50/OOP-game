from Exceptions.NotAllowedWeaponException import NotAllowedWeaponException
from Exceptions.MaxSpaceBackpackException import BackpackSpaceReachedException
from Exceptions.NoWeaponException import NoWeaponException

class Heroj(object):

    def __init__(self, weapon_in_hand, backpack = []):
        self.health = 0
        self.weapon_in_hand = weapon_in_hand
        self.backpack = backpack

    def __str__(self):
        return f"{self.health}\n{self.weapon_in_hand}\n{self.backpack}"

    def dodaje_u_ranac(self, weapon):
        if len(self.backpack) == 2:
            raise BackpackSpaceReachedException()
        self.backpack.append(weapon)
        return self.backpack

    def napad(self, target):
        target.health = target.health - self.weapon_in_hand.damage
        return target.health

    def uzima_oruzje(self, weapon):
        self.weapon_in_hand = weapon
        return self.weapon_in_hand

    def baca_oruzje(self):
        self.weapon_in_hand = None
        self.weapon_in_hand = self.backpack[0]
        self.backpack.pop(0)
        return self.weapon_in_hand

    def menja_oruzje(self, index):
        if len(self.backpack) == 0:
            raise NoWeaponException()
        else:
            self.weapon_in_hand = self.backpack[index]
            self.backpack.pop(index)  
            return f"{self.weapon_in_hand}\n{self.backpack}"


class Oruzje:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name



class Carobnjak(Heroj):
    
    def __init__(self, weapon_in_hand, backpack):
        Heroj.__init__(self, weapon_in_hand, backpack)
        self.health = 150

        
    def uzima_oruzje(self, weapon):
        if weapon.name == "Mac" or weapon.name == "Koplje":
            raise NotAllowedWeaponException()
        else:
            self.weapon_in_hand = weapon
    

        


class Macevalac(Heroj):

    def __init__(self, weapon_in_hand, backpack):
        Heroj.__init__(self, weapon_in_hand, backpack)
        self.health = 100

    def uzima_oruzje(self, weapon):
        if weapon.name == "Carolija":
            raise NotAllowedWeaponException()
        else:
            self.weapon_in_hand = weapon