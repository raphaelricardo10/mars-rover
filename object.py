import re

#A object is anything that can be inserted in the space
class Object:
    #Stores all the objects deployed
    lstObj = []
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.id = len(Object.lstObj)

        self._startX = self.x
        self._startY = self.y

        Object.lstObj.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"[a-zA-Z]+$", value):
            self._name = value
        else:
            raise ValueError("The name attribute may have only a-z characters")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value >= 0:
            self._x = value
        else:
            raise ValueError("The x attribute cannot be negative")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value >= 0:
            self._y = value
        else:
            raise ValueError("The y attribute cannot be negative")