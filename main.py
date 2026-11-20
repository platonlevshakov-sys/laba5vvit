from garage import Garage
from models import Car,Truck,Motorcycle,Bus
def main():
    car = Car("Toyota", "Camry", 2020, 4)
    truck = Truck("Volvo", "FH", 2022, 20000)
    motorcycle = Motorcycle("Honda", "CBR", 2021, False)
    bus = Bus("ЛиАЗ", "5292", 2019, 100)

    car.accelerate(60)
    car.brake(20)
    truck.accelerate(40)

    vehicles = [car, truck, motorcycle, bus]

    print("Информация о транспортных средствах:")
    for vehicle in vehicles:
        print(vehicle.get_info())
        print(vehicle.move())

    print("\nПроверка остановки автомобиля:")
    car.stop()
    print(car)

    print("\nПроверка обработки отрицательной скорости:")
    try:
        car.speed = -10
    except ValueError as error:
        print(f"Ошибка: {error}")

    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)

    print("\nСодержимое гаража:")
    garage.show_all()

    print("\nПоиск транспорта марки Toyota:")
    for vehicle in garage.find_by_brand("Toyota"):
        print(vehicle)


if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
