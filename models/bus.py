from .vehicle import Vehicle
class Bus(Vehicle):
    def __init__(self, brand, model, year, passenger_capacity):
        super().__init__(brand,model,year)
        self.passenger_capacity = passenger_capacity
    def get_info(self):
        return f"{super().get_info()}, вместимость: {self.passenger_capacity} пассажиров"
    def move(self):
        return f"Автобус {self.brand} перевозит пассажиров"


