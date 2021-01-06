class Ship:
    def __init__(self, shipType, length, timesHit, isDestroyed = False, symbol = "X"):
        self.shipType = shipType
        self.length = length
        self.timesHit = timesHit
        self.isDestroyed = isDestroyed
        self.symbol = symbol

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
    
    def GetSymbol(self):
        return self.symbol


class Submarine(Ship):
    def __init__(self, timesHit, symbol = 'S'):
        super().__init__("Submarine", 2, timesHit)
        self.symbol = symbol
        

class Battleship(Ship):
    def __init__(self, timesHit, symbol = 'B'):
        super().__init__("Battleship", 3, timesHit)
        self.symbol = symbol

class Destroyer(Ship):
    def __init__(self, timesHit, symbol = 'D'):
        super().__init__("Destroyer", 4, timesHit)
        self.symbol = symbol

class AircraftCarrier(Ship):
    def __init__(self, timesHit, symbol = 'A'):
        super().__init__("Aircraft Carrier", 5, timesHit)
        self.symbol = symbol

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
        for i in range(8):
            arr = []
            for item in self.board[i]:
                if item.GetShip() == None:
                    arr.append("~")
                else:
                    arr.append(item.GetShip().GetSymbol())
            print(str(8-i) + "  %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s " % (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7]))
        print("   %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s " % ("A", "B", "C", "D", "E", "F", "G", "H"))
    
    def PlaceShip(self, x, y, ship, rotation):
        for i in range(ship.GetLength()):
            if rotation == "Horizontal":
                self.board[7-y][x+i] = Location(x, y+i, ship)
            else:
                self.board[7-(y+i)][x] = Location(x+i, y, ship)


class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ships = []
        self.ships.extend((AircraftCarrier(0), Destroyer(0), Destroyer(0), Battleship(0), Battleship(0), Battleship(0), Submarine(0)))
    
    def PlaceShip(self, x, y, orientation, shipNo):
        self.board.PlaceShip(x,y, self.ships[shipNo], orientation)
        self.board.DisplayBoard()

p1 = Player(input("Name: "))

for i in range(7):
    positionStr = input("Where would you like your " + p1.ships[i].GetShipType() +" (length: " +str(p1.ships[i].GetLength()) + ") to go on the x axis e.g. 'A1':")

    x = ord(positionStr[0].upper()) - 65
    y = int(positionStr[1])-1

    choice = input("Would you like it to be \n1: Horizontal\n2: Vertical")
    if choice == "1":
        orientation = "Horizontal"
    else:
        orientation = "Vertical"
    p1.PlaceShip(x, y, orientation, i)