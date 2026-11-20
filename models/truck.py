from.vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self,brand,model,year,max_load):
        super().__init__(brand,model,year)
        self.max_load = max_load
    def get_info(self):
        return f"{super().get_info()}, грузоподъемность: {self.max_load} кг"
    def move(self):
        return f"Грузовик {self.brand} перевозит груз"
