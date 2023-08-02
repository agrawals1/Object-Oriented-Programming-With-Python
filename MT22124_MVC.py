# Model

class Numbers():

    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

class Calculator():
    
    def __init__(self, numbers) -> None:
        self.num1 = numbers.num1
        self.num2 = numbers.num2

    def Add(self):
        return self.num1 + self.num2

    def Subtract(self):
        return self.num1 - self.num2    

    def Multiply(self):
        return self.num1*self.num2

    def Divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        return "divide by 0 occured"   

#  View
class View:

    def show(self, result):
        print(result)         


# Controller
if __name__ == "__main__":

    numbers = Numbers(4,0)
    calc = Calculator(numbers)
    view = View()
    view.show(calc.Add())
    view.show(calc.Subtract())
    view.show(calc.Multiply())
    view.show(calc.Divide())