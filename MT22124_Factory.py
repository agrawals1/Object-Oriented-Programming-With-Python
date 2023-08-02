from abc import ABC, abstractmethod

# Model

class Operation(ABC):

    """Parent class for all the calculator operations"""

    @abstractmethod
    def operate(self, x, y):
        pass
        

class AddInt(Operation):

    def operate(self, x, y):
        x = int(x)
        y = int(y)
        return x+y

class AddFloat(Operation):

    def operate(self, x, y):
        x = float(x)
        y = float(y)
        return x+y

class SubInt(Operation):

    def operate(self, x, y):
        x = int(x)
        y = int(y)
        return float(x-y)  

class SubFloat(Operation):

    def operate(self, x, y):
        x = float(x)
        y = float(y)
        return float(x-y)

class MulInt(Operation):

    def operate(self, x, y):
        x = int(x)
        y = int(y)
        return float(x*y)  

class MulFloat(Operation):

    def operate(self, x, y):
        x = float(x)
        y = float(y)
        return float(x*y)

class DivInt(Operation):

    def operate(self, x, y):
        x = int(x)
        y = int(y)
        try:
            assert y!=0
        except:
            print("Divide by 0 not allowed")
            exit()    
        return int(x/y)  

class DivFloat(Operation):

    def operate(self, x, y):
        x = float(x)
        y = float(y)
        try:
            assert y!=0
        except:
            print("Divide by 0 not allowed")
            exit()  
        return x/y

# View
class View:

    """View for Int and Float results"""

    def show(self, result):
        pass

class IntView(View):

    def show(self, result):
        print("Result is : " + str(int(result)))


class FloatView(View):

    def show(self, result):
        print("Result is : " + str(float(result)))        

                                
class ViewFactory:

    """Factory to instantiate view objects"""

    views = {'int': IntView, 'float': FloatView}

    # Instantiate the correct view
    def getView(self, dtype):
        myview = self.views[dtype]
        return myview()

    # Easily add new views to the factory through this method
    def addView(self, dtype, viewClass):        
        self.views[dtype] = viewClass  


class CalFactory:
    """Factory to instantiate calculator operations"""

    operations = {'addint': AddInt, 'subint': SubInt, 'mulint': MulInt, 'divint': DivInt,
                    'addfloat': AddFloat, 'subfloat':SubFloat, 'mulfloat': MulFloat, 'divfloat': DivFloat}

    # Instantiate the correct operator
    def getOperation(self, op, dtype):
        myop = self.operations[op+dtype]
        return myop()

    # Easily Add new operations to the factory through this method
    def addOperation(self, op, dtype, opClass):
        self.operations[op+dtype] = opClass       
    
        
 

# Controller

if __name__ == "__main__":

    while(True):
        
        op = input("""Enter the operations:- add for addition, sub. for subtraction, 
                      mul for multiplication, div for division\n""")
        dtype = input("Enter float or int")

        x = input("Enter first number")
        y = input("Enter second number") 

        # Create factories
        factoryCal = CalFactory()   
        factoryView = ViewFactory()

        # Get the objects through factories
        calobj = factoryCal.getOperation(op, dtype)
        view = factoryView.getView(dtype)

        # Operate and show results
        result = calobj.operate(x, y)
        view.show(result)
