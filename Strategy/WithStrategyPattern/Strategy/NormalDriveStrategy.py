from WithStrategyPattern.Strategy.DriveStrategy import DriveStrategy

class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        # Normal Drive Strategy 
        print("Normal Drive Strategy")