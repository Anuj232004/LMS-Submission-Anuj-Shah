from task1 import Vehicle

class Car(Vehicle):
    def __init__ (self,brand,model,year,price,number_of_doors):
        super().__init__(brand,model,year,price)
        self.number_of_doors=number_of_doors
    
    def display_info(self):
        print(f"The name of brand is:{self.brand} of model:{self.model} of year:{self.year} of price:{self.price} with number_of doors as: {self.number_of_doors}")

def main():
    c1=Car("toyota","fortuner","2015",5000000.00,4)
    c1.display_info()


if __name__=="__main__":
    main()