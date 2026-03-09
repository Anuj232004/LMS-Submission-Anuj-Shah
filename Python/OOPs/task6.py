from task1 import Vehicle

class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}")

    # Method overloading using *args
    def calculate_discount(self, *args):
        if len(args) == 1:
            discount = args[0]
            final_price = self.price * (1 - discount / 100)
            return final_price
        elif len(args) == 2:
            discount, additional_discount = args
            final_price = self.price * (1 - discount / 100)
            final_price *= (1 - additional_discount / 100)
            return final_price
        else:
            return self.price


def main():
    car1 = Vehicle("Toyota", "Fortuner", "2015", 5000000.00)
    car1.display_info()

    print("Price after 10% discount:", car1.calculate_discount(10))
    print("Price after 10% + 5% additional discount:", car1.calculate_discount(10, 5))


if __name__ == "__main__":
    main()