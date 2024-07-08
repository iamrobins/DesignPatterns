from typing import Any
from abc import ABC, abstractmethod

class Car:  # Product1
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print("Car Parts: ", self.parts)

class Manual:  # Product2
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print("Car Manual: ", self.parts)

class Builder(ABC):  # Builder

    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def setSeats(self, seats):
        pass

    @abstractmethod
    def setEngine(self, engine):
        pass

    @abstractmethod
    def setTripComputer(self, trip_computer):
        pass

    @abstractmethod
    def setGPS(self, gps):
        pass

class CarBuilder(Builder):  # ConcreteBuilder1
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def setSeats(self, seats):
        self._car.add({"Seat": seats})

    def setEngine(self, engine):
        self._car.add({"Engine": engine})

    def setTripComputer(self, trip_computer):
        self._car.add({"Trip": trip_computer})

    def setGPS(self, gps):
        self._car.add({"GPS": gps})

    def getProduct(self):
        product = self._car
        self.reset()
        return product

class CarManualBuilder(Builder):  # ConcreteBuilder2
    def __init__(self):
        self.reset()

    def reset(self):
        self._manual = Manual()

    def setSeats(self, seats):
        self._manual.add({"Seat": seats})

    def setEngine(self, engine):
        self._manual.add({"Engine": engine})

    def setTripComputer(self, trip_computer):
        self._manual.add({"Trip": trip_computer})

    def setGPS(self, gps):
        self._manual.add({"GPS": gps})

    def getProduct(self):
        product = self._manual
        self.reset()
        return product

class Director:  # Director
    def constructSportsCar(self, builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine("SportEngine")
        builder.setTripComputer(True)
        builder.setGPS(True)

    def constructSUV(self, builder):
        pass

class Application:  # Client
    def makeCar(self):
        director = Director()

        builder = CarBuilder()  # ConcreteBuilder1
        director.constructSportsCar(builder)
        car = builder.getProduct()
        car.list_parts()

        builder = CarManualBuilder()  # ConcreteBuilder2
        director.constructSportsCar(builder) # Because we making the manual for sports car
        manual = builder.getProduct()
        manual.list_parts()


app = Application()
app.makeCar()