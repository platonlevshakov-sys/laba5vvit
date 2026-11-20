from .vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,has_sidecar = False):
        super().__init__(brand,model,year)
        self.has_sidecar = has_sidecar
    def get_info(self):
        sidecar = "есть" if self.has_sidecar else "нет"
        return f"{super().get_info()}, коляска: {sidecar}"
    def move(self):
        return f"Мотоцикл {self.brand} движется по дороге"
