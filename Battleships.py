class Ship:
    def __init__(self, shipType, length, timesHit):
        self.shipType = shipType
        self.length = length
        self.timesHit = timesHit
        self.isDestroyed = True