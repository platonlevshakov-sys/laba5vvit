from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,value):
        if value < 0:
            raise ValueError("Скорость не может быть < 0")
        self._speed = value
    def accelerate(self, value):
        if value < 0:
            raise ValueError("Ускорение не может быть < 0")
        self._speed += value
    def brake(self, value):
        if value < 0:
            raise ValueError("Торможение не может быть < 0")
        self._speed = max(0,self.speed - value)
    def stop(self):
        self.speed = 0
    def get_info(self):
        return f'{self.brand} {self.model} {self.year} г., скорость: {self.speed} км/ч'
    @abstractmethod
    def move(self):
        pass
    def __str__(self):
        return self.get_info()

