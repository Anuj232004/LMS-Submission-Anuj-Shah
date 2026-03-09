from task1 import Vehicle

class Vehicle:
    def __init__(self,price=0):
        self.__price=price

    def get_price(self):
        return self.__price
    
    def set_price(self,price=0):
        try:
            if price>0:
               self.__price=price
        except TypeError:
            print("Invalid Value")

car1=Vehicle()
car1.set_price(50000)
print(car1.get_price())
     