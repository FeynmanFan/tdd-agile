from src.lifesupport import LifeSupportSystem
from src.o2tank import o2tank

class LifeSupportSystemFacade:
    def __init__(self):
        self._life_support = LifeSupportSystem(isActive=True)
        self._tank = o2tank(0)

    @property
    def level(self):
        return self._tank.level

    @level.setter
    def level(self, value):
        self._tank.level = value
