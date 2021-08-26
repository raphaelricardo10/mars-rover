from itertools import count, cycle
from typing import Deque
from plateau import Plateau
from object import Object

#Implement rover as a object
class Rover(Object):

    #It is used to increase the code readability
    class Orientation:
        #Indexes all the supported orientations to a make cleaner rotation code
        #Cycle is used for efficient rotations to get the next and previous orientations
        _head = Deque(['N', 'E', 'S', 'O'])

        #Orientation class constructor
        def __init__(self, current) -> None:
            if current not in self._head:
                raise ValueError(f"Orientation '{current}' is not allowed")
            self.current = current



    #Rover class constructor
    def __init__(self, plat: Plateau, x: int, y: int, orientation: Orientation, instructions: str) -> None:
        super(Rover, self).__init__("Rover", x, y)
        self.Orientation = Rover.Orientation(orientation)
        self.instructions = instructions
        plat.insert(self)

        self._startX = x
        self._startY = y

    #Moves the rover to the first point in front of it
    def moveFwd(self, plat: Plateau) -> None:
        plat.remove(self)

        if self.Orientation.current == 'N':
            self.y += 1
        elif self.Orientation.current == 'E':
            self.x += 1
        elif self.Orientation.current == 'S':
            self.y -= 1
        elif self.Orientation.current == 'O':
            self.x -= 1
        else:
            raise ValueError(f"Orientation '{self.Orientation.current}' is not allowed")

        try:
            plat.checkPt(self.x, self.y)

        except Exception:
            raise

        finally:
            plat.insert(self)

    #Rotate a rover right or left using R or L char respectively
    def rotate(self, direction: str) -> None:
        #Matches the Deque head with the current orientation
        while self.Orientation._head[0] != self.Orientation.current:
            self.Orientation._head.rotate(1)

        if direction.upper() == 'L':
            self.Orientation._head.rotate(1)
            self.Orientation.current  = self.Orientation._head[0]
        else:
            self.Orientation._head.rotate(-1)
            self.Orientation.current  = self.Orientation._head[0]

    #Execute the instructions stored in the rover
    def execInst(self, plat: Plateau) -> None:
        try:
            for instruction in self.instructions:
                if instruction.upper() == 'M':
                    self.moveFwd(plat)
                elif instruction.upper() == 'R' or instruction.upper() == 'L':
                    self.rotate(instruction)
                else:
                    raise ValueError(f"Unexpected instruction value: {instruction}")
        
        #Forwards the exceptions to the driver program
        except Exception:
            raise

    def cancelMov(self) -> None:
        self.x = self._startX
        self.y = self._startY

    #Gets the rover position
    def getPos(self) -> list:
        return [self.x, self.y]