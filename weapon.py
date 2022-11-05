class Weapon:
    def __init__(self, range :int ,ammunition:int):
        self.ammunition = ammunition
        self.range= range

#Méthode qui permet de tirer à un endroit précis

    def fire_at(self, x:int, y:int , z:int):
        self.x = x
        self.y = y
        self.z = z

import weapon as Weapon

class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        self._ammunition= 3
        self._range= 30


    def fire_at(self, x: int, y: int,z : int):
        if z == 0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                return NoAmmunitionError
        else :
          return OutOfRangeError


class Lance_missiles_antiair(Weapon):
    def __init__(self):
        self._ammunition= 50
        self._range= 40


    def fire_at(self, x: int, y: int, z: int):
        if z>0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                return NoAmmunitionError
        else:
            return OutOfRangeError

class Lance_Torpilles(Weapon):
    def __init__(self):
        self._ammunition= 15
        self._range= 20


    def fire_at(self, x: int, y: int, z: int):
        if z<0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                return NoAmmunitionError

