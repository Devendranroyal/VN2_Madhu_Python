class Bike:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    def get_bike_details(self):
        print("Bike details : ",self.brand,self.color,self.price)