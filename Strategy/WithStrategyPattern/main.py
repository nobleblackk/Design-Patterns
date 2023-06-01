# from PassangerVehicle import PassngerVehicle 
# from SportVehicle import SportVehicle
# from Strategy.DriveStrategy import DriveStrategy
# from Strategy.NormalDriveStrategy import NormalDriveStrategy
# from Strategy.SportDriveStrategy import SportDriveStrategy
# from WithStrategyPattern.OffRoadVehicle import OffRoadVehicle


# vehicle_a = OffRoadVehicle() 
# vehicle_a.drive()

# vehicle_b = SportVehicle() 
# vehicle_b.drive()

# vehicle_c = PassangerVehicle()
# vehicle_c.drive()




################### Here is the Strategy Pattern Inline

class DriveStrategy:
    
    def drive(self):
        # here classes will implement this functionality
        pass



class SportDriveStrategy(DriveStrategy):

    def drive(self):
        # Sport Drive Strategy 
        print("Sport Drive Strategy")

class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal Drive Strategy")


class Vehicle:

    def __init__(self, driveStrategyObj = None):
        self.driveStrategyObj = driveStrategyObj

    def drive(self):
        self.driveStrategyObj.drive()




class OffRoadVehicle(Vehicle):

    def __init__(self, driveStrategyObj=None):
        super().__init__(driveStrategyObj=SportDriveStrategy())

class SportVehicle(Vehicle):
    def __init__(self):
        super().__init__(driveStrategyObj=NormalDriveStrategy())

vehicle_a = OffRoadVehicle() 
vehicle_a.drive()

vehicle_b = SportVehicle()
vehicle_b.drive()