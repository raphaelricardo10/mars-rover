#Implements a plateau with a grid system
from object import Object

class Plateau:

    class Error(Exception):
        "Base class for other exceptions"
        pass

    class OutOfLimitsError(Error):
        "Raised when a instruction moves a object to off limits"
        pass

    class CollisionDetectedError(Error):
        "Raised when a instruction causes a collision between two objects"
        pass


    #Implements the size of the grid in a separate class for a better readability
    class Limits:
        #Limits class constructor
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

    #Plateau class constructor
    def __init__(self, xLimit: int, yLimit: int) -> None:
        Plateau.Limits = Plateau.Limits(xLimit, yLimit)
        #False represents a empty space in the grid
        self.grid = [[False for x in range(xLimit+1)] for y in range(yLimit+1)]

    #insert a object in the grid
    def insert(self, obj: Object) -> None:
        self.grid[obj.x][obj.y] = obj

    #Removes a object from the grid
    def remove(self, obj: Object) -> None:
        if obj is self.grid[obj.x][obj.y]:
            self.grid[obj.x][obj.y] = False
        else:
            raise Exception(f"The object {object.name} {object.id} does not exist in [{object.x},{object.y}]")

    #Checks if the selected point is available to deploy a object
    def checkPt(self, x, y) -> None:

            if x > self.Limits.x or y > self.Limits.y or x < 0 or y < 0:
                raise Plateau.OutOfLimitsError(f"The point [{x},{y}] is off limits")

            if False not in [self.grid[0][x],self.grid[1][y]]:
                raise Plateau.CollisionDetectedError(f"The point [{x},{y}] is already occupied")
