class Plateau:
    def __init__(self, xLimit, yLimit) -> None:
        self.xLimit = xLimit
        self.yLimit = yLimit
        self.grid = [[False]*xLimit, [False]*yLimit]

    def insertObject(self, type, x , y) -> None:
        self.grid[0].insert(x, type)
        self.grid[1].insert(y, type)