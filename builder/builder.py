from typing import Any
from abc import ABC, abstractmethod

class Computer:  # Product1
    def __init__(self) -> None:
        self.parts: list[dict[str, Any]] = []

    def add(self, part: dict[str, Any]) -> None:
        k: str = list(part.keys())[0]
        v: str = list(part.values())[0]
        for p in self.parts:
            if k in p:
                p[k] = v
                return
        self.parts.append(part)

    def list_parts(self) -> None:
        print("Computer Parts: ", self.parts)

class Manual:  # Product2
    def __init__(self) -> None:
        self.parts: list[dict[str, Any]] = []

    def add(self, part: dict[str, Any]) -> None:
        k: str = list(part.keys())[0]
        v: str = list(part.values())[0]
        for p in self.parts:
            if k in p:
                p[k] = v
                return
        self.parts.append(part)

    def list_parts(self) -> None:
        print("Computer Manual: ", self.parts)

class Builder(ABC):  # Builder

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setCPU(self, cpu: str):
        pass

    @abstractmethod
    def setRAM(self, ram: int):
        pass

    @abstractmethod
    def setStorage(self, storage: str):
        pass

    @abstractmethod
    def setGPU(self, gpu: str):
        pass

    @abstractmethod
    def setPowerSupply(self, power_supply: str):
        pass

class ComputerBuilder(Builder):  # ConcreteBuilder1
    def __init__(self):
        self.reset()

    def reset(self):
        self._computer = Computer()

    def setCPU(self, cpu: str):
        self._computer.add({"CPU": cpu})

    def setRAM(self, ram: int):
        self._computer.add({"RAM": ram})

    def setStorage(self, storage: str):
        self._computer.add({"Storage": storage})

    def setGPU(self, gpu: str):
        self._computer.add({"GPU": gpu})

    def setPowerSupply(self, power_supply: str):
        self._computer.add({"Power Supply": power_supply})

    def getProduct(self):
        product = self._computer
        self.reset()
        return product

class ComputerManualBuilder(Builder):  # ConcreteBuilder2
    def __init__(self):
        self.reset()

    def reset(self):
        self._manual = Manual()

    def setCPU(self, cpu: str):
        self._manual.add({"CPU": cpu})

    def setRAM(self, ram: int):
        self._manual.add({"RAM": ram})

    def setStorage(self, storage: str):
        self._manual.add({"Storage": storage})

    def setGPU(self, gpu: str):
        self._manual.add({"GPU": gpu})

    def setPowerSupply(self, power_supply: str):
        self._manual.add({"Power Supply": power_supply})

    def getProduct(self):
        product = self._manual
        self.reset()
        return product

class Director:  # Director
    def constructGamingPC(self, builder: Builder):
        builder.reset()
        builder.setCPU("High-End CPU")
        builder.setRAM(32)
        builder.setStorage("1TB SSD")
        builder.setGPU("High-End GPU")
        builder.setPowerSupply("750W")

    def constructNormalPC(self, builder: Builder):
        builder.reset()
        builder.setCPU("Noraml CPU")
        builder.setRAM(8)
        builder.setStorage("256 SSD")
        builder.setGPU("Integrated GPU")
        builder.setPowerSupply("550W")

    def constructOfficePC(self, builder: Builder):
        builder.reset()
        builder.setCPU("Mid-Range CPU")
        builder.setRAM(16)
        builder.setStorage("512GB SSD")
        builder.setGPU("Integrated GPU")
        builder.setPowerSupply("500W")

class Application:  # Client
    def makeComputer(self):
        director = Director()

        builder = ComputerBuilder()  # ConcreteBuilder1
        director.constructGamingPC(builder)
        # builder.setRAM(64) # Customisation
        computer = builder.getProduct()
        computer.list_parts()

        builder = ComputerManualBuilder()  # ConcreteBuilder2
        director.constructGamingPC(builder)  # Because we are making the manual for gaming PC
        manual = builder.getProduct()
        manual.list_parts()

app = Application()
app.makeComputer()