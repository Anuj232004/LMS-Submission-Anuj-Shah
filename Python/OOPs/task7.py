class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}")

    # Save vehicle details to a file
    def save_to_file(self):
        filename = f"{self.brand}_{self.model}.txt"
        with open(filename, "w") as f:
            f.write(f"Brand: {self.brand}\n")
            f.write(f"Model: {self.model}\n")
            f.write(f"Year: {self.year}\n")
            f.write(f"Price: {self.price}\n")
        print(f"Vehicle details saved to {filename}")


def main():
    car1 = Vehicle("Honda", "Civic", "2018", 2200000.00)
    car1.display_info()
    car1.save_to_file()


if __name__ == "__main__":
    main()