from abc import ABC, abstractmethod

class Beverage(ABC):

    description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass   

class Cappucino(Beverage):

    def __init__(self):
        description = "Cappucino"

    def cost(self):
        return 2.0    

class CondimentDecorator(Beverage, ABC):

    beverage : Beverage

    @abstractmethod
    def getDescription():
        pass


class Caramel(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
           return self.beverage.getDescription() + ", Caramel"

    def cost(self):
        return 0.5 + self.beverage.cost()

class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
           return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()

if __name__ == "__main__":

    cappucino = Cappucino()
    caramel_capp = Caramel(cappucino)
    whip_caramel_capp = Whip(caramel_capp)

    print(whip_caramel_capp.cost())