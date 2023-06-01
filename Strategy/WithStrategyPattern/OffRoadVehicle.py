from WithStrategyPattern.Vehicle import Vehicle
from WithStrategyPattern.Strategy.SportDriveStrategy import SportDriveStrategy

class OffRoadVehicle(Vehicle):

    def __init__(self, driveStrategyObj=None):
        super().__init__(driveStrategyObj=SportDriveStrategy())

    