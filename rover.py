class Rover:

    cardinals = ['N', 'E', 'S', 'O']
    cardinalsDict = {}

    def __init__(self, orientation, x, y) -> None:
        self.x = x
        self.y = y

        index
        for i in Rover.cardinals:
            Rover.orientations[orientation] = Rover.cardinals

        self.orientation = cardinalsDict[]

    def move(self, plateau):
        plateau.removeObject(self.x, self.y)

        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'S':
            self.y += 1
        elif self.orientation == 'O':
            self.x -= 1
        else:
            print("Error in function move(): orientation \"{0}\" is not allowed", self.orientation)
            plateau.insertObject("Rover", self.x, self.y)
            return -1

        plateau.insertObject("Rover", self.x, self.y)

    def rotate(self):
        self.orientation = cardinalsDict[]