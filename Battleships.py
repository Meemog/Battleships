import re
import random

class Ship:
    def __init__(self, shipType, length, timesHit, symbol = "X"):
        self.shipType = shipType
        self.length = length
        self.timesHit = timesHit
        self.symbol = symbol
        self.isDestroyed = False

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
        for i in range(10):
            row = []
            for j in range(10):
                location = Location(i, j)
                row.append(location)
            self.board.append(row)
    
    def DisplayBoard(self):
        for i in range(10):
            arr = []
            for item in self.board[i]:
                if item.GetShip() == None:
                    arr.append("~")
                else:
                    arr.append(item.GetShip().GetSymbol())
            print("%2s  %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s " % (str(10-i), arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9]))
        print("%2s  %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s " % ("", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"))
    
    def PlaceShip(self, x, y, ship, rotation):
        for i in range(ship.GetLength()):
            if rotation == "Horizontal":
                if self.board[9-y][x+i].GetShip() != None:
                    return False
            else:
                if self.board[9-(y+i)][x].GetShip() != None:
                    return False

        for i in range(ship.GetLength()):
            if rotation == "Horizontal":
                self.board[9-y][x+i] = Location(x, y+i, ship)
            else:
                self.board[9-(y+i)][x] = Location(x+i, y, ship)
        return True


class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ships = []
        self.ships.extend((AircraftCarrier(0), Destroyer(0), Destroyer(0), Battleship(0), Battleship(0), Battleship(0), Submarine(0)))
    
    def PlaceShip(self, x, y, orientation, shipNo):
        x = self.board.PlaceShip(x,y, self.ships[shipNo], orientation)
        return x 

p1 = Player(input("Name: "))

valid = False
while valid == False:
    boardPos = input("Would you like to\n1: place ships manually or \n2: have the computer do it for you")
    if boardPos == "1" or boardPos == "2":
        valid = True
    else:
        print("Please enter either '1' or '2'")

if boardPos == "1":
    for i in range(7):

        p1.board.DisplayBoard()
        
        check = False

        while check == False:
            valid = False
            while valid == False:
                positionStr = input("Where would you like your " + p1.ships[i].GetShipType() +" (length: " +str(p1.ships[i].GetLength()) + ") to go on the x axis e.g. 'A1':")

                if re.search("[A-Ja-j][1-10]", positionStr) == None:
                    print("Enter a value between A1 and J10")
                else:
                    valid = True
            
            
            x = ord(positionStr[0].upper()) - 65
            y = int(positionStr[1])-1

            valid = False
            while valid == False:
                choice = input("Would you like it to be \n1: Horizontal\n2: Vertical")
                if choice == "1":
                    orientation = "Horizontal"
                    valid = True
                elif choice == "2":
                    orientation = "Vertical"
                    valid = True
                else:
                    print("Please enter 1 or 2")

            if choice == "1":
                if (x + p1.ships[i].GetLength()) > 10:
                    print("That ship doesn't fit there")
                else:
                    check = True
            elif choice == "2":
                if (y + p1.ships[i].GetLength()) > 10:
                    print("That ship doesn't fit there")
                else:
                    check = True
        if p1.PlaceShip(x, y, orientation, i) == False:
            check = False
            print("That ship doesn't fit there")
    p1.board.DisplayBoard()

else:
    for i in range(7):
        valid = False
        while valid == False:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.choice(["Horizontal", "Vertical"])

            valid = True

            if orientation == "Horizontal":
                if (x + p1.ships[i].GetLength()) > 10:
                    valid = False
            elif orientation == "Vertical":
                if (y + p1.ships[i].GetLength()) > 10:
                    valid = False
            if valid == True:
                if p1.PlaceShip(x, y, orientation, i) == False:
                    valid = False
    p1.board.DisplayBoard()
