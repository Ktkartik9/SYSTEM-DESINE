from typing import Optional


class Engine:
    def __init__(self, engine_type, horsepower) -> None:
        self.__engine_type = engine_type
        self.__horsepower = horsepower

    def get_details(self) -> str:
        return f"{self.__engine_type} Engine ({self.__horsepower} HP)"

    def start(self) -> None:
        print(f"{self.__engine_type} engine started!")



class Car:
    def __init__(self, brand, model, engine_type, horsepower) -> None:
        self.__brand: str = brand
        self.__model: str = model

        self.__engine = Engine(engine_type, horsepower)

    def get_car_details(self) -> None:
        print(f"\nCar: {self.__brand} {self.__model}")
        print(f"Engine: {self.__engine.get_details()}")

    def start_car(self) -> None:
        print(f"\nStarting {self.__brand} {self.__model}...")
        self.__engine.start()
        print("Car is ready to drive!")



my_car: Car = Car("Toyota", "Fortuner", "Diesel", 204)
my_car.get_car_details()

my_car.start_car()


print("\n--- Destroying the car ---")
del my_car  


print("Car and its Engine are both destroyed!")