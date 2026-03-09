from task1 import Vehicle
from task3 import Car

class Bike(Vehicle):
    def __init__ (self,brand,model,year,price):
        super().__init__(brand,model,year,price)
    
    def display_info(self):
        print(f"The name of bike brand is:{self.brand} of model:{self.model} of year:{self.year} of price:{self.price}")

v=Vehicle("toyota","fortuner","2015",5000000.00)
c=Car("toyota","fortuner","2023",3500000.00,5)
b=Bike("suzuki","mt5","2018",500000.00)

v.display_info()
c.display_info()
b.display_info()