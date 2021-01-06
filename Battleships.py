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
