class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print(f"The name of brand is:{self.brand} of model:{self.model} of year:{self.year} of price:{self.price}")
    
def main():
    car1=Vehicle("toyota","fortuner","2015",5000000.00)
    car1.display_info()



if __name__=="__main__":
    main()