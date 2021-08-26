#A object is anything that can be inserted in the space
class Object:
    #Stores all the objects deployed
    lstObj = []
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.id = len(Object.lstObj)
        Object.lstObj.append(self)