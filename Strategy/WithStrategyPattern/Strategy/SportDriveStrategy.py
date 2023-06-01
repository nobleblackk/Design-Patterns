from WithStrategyPattern.Strategy.DriveStrategy import DriveStrategy

class SportDriveStrategy(DriveStrategy):

    def drive(self):
        # Sport Drive Strategy 
        print("Sport Drive Strategy")