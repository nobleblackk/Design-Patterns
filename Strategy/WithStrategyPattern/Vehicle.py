# from WithStrategyPattern.Strategy.DriveStrategy import DriveStrategy

class Vehicle:

    def __init__(self, driveStrategyObj = None):
        self.driveStrategyObj = driveStrategyObj

    def drive(self):
        self.driveStrategyObj.drive()