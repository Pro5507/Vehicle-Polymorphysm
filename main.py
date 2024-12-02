class BMW:
    def __init__(self, speed, price):
        self.price = price
        self.speed = speed

    def display_info(self):
        return f"BMW with speed {self.speed} km/h and price {self.price} dollars."

class Farrari(BMW):
    def __init__(self, speed, price):
        super().__init__(speed, price)

    def display_info(self):
        return f"Farrari with speed {self.speed} km/h and price {self.price} dollars."

def show_car_info(car):
    print(car.display_info())

a = BMW(250, 500000000)
b = Farrari(300, 700000000)

show_car_info(a)
show_car_info(b)
