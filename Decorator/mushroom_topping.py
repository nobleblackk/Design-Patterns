from topping import Topping

class MushroomTopping(Topping):

    def __init__(self, pizza):
        super().__init__(pizza)

    
    def cost(self):
        return self.pizza.cost() + 10
