class Ship:
    def __init__(self, shipType, length, timesHit, isDestroyed = False):
        self.shipType = shipType
        self.length = length
        self.timesHit = timesHit
        self.isDestroyed = isDestroyed

    def GetShipType(self):
        return self.shipType

    def GetLength(self):
        return self.length

    def GetTimesHit(self):
        return self.timesHit

    def SetTimesHit(self, value):
        self.timesHit = value
    
    def GetIsDestroyed(self):
        return self.isDestroyed
    
    def SetIsDestroyed(self, value):
        self.isDestroyed = value


class Submarine(Ship):
    def __init__(self, timesHit):
        super().__init__("Submarine", 2, timesHit)

class Battleship(Ship):
    def __init__(self, timesHit):
        super().__init__("Battleship", 3, timesHit)

class Destroyer(Ship):
    def __init__(self, timesHit):
        super().__init__("Destroyer", 4, timesHit)

class AircraftCarrier(Ship):
    def __init__(self, timesHit):
        super().__init__("Aircraft Carrier", 5, timesHit)

class Location:
    def __init__(self, x, y, ship = None):
        self.x = x
        self.y = y
        self.ship = ship
    
    def GetX(self):
        return self.x

    def GetY(self):
        return self.y
    
    def GetShip(self):
        return self.ship

class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                location = Location(i, j)
                row.append(location)
            self.board.append(row)
    def DisplayBoard(self):
        for row in self.board:
            arr = []
            for item in row:
                if item.GetShip() == None:
                    arr.append("~")
            print("%-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s " % (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7]))


b1 = Board()

b1.DisplayBoard()