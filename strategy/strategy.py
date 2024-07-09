from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    
    @abstractmethod
    def collectPaymentDetails(self):
        pass

    @abstractmethod
    def validatePaymentDetails(self) -> bool:
        pass

    @abstractmethod
    def pay(self, amount: int):
        pass

class PaymentByPayPal(PaymentStrategy):
    def collectPaymentDetails(self):
        email = ".."
        password = "..."
    
    def validatePaymentDetails(self) -> bool:
        return True

    def pay(self, amount: int):
        print(f"Paid amount {amount} using PayPal")

class PaymentByCreditCard(PaymentStrategy):
    def collectPaymentDetails(self):
        card_no = ".."
        expiry_date = "..."
        cvv = "...."

    def validatePaymentDetails(self) -> bool:
        return True

    def pay(self, amount: int):
        print(f"Paid amount {amount} using Credit Card")

class PaymentService:
    def __init__(self) -> None:
        self.__cost: int = None
        self.__include_delivery: bool = False
        self.__strategy: PaymentStrategy = None
    
    def process_order(self):
        self.__strategy.collectPaymentDetails()
        if self.__strategy.validatePaymentDetails():
            self.__strategy.pay(self.get_total())

    def get_total(self) -> int:
        return self.__cost + 10 if self.__include_delivery else self.__cost
    
    def set_strategy(self, strategy):
        self.__strategy = strategy
    
    def set_cost(self, cost):
        self.__cost = cost

    def set_delivery(self, delivery):
        self.__include_delivery = delivery

payment_service = PaymentService()
payment_service.set_cost(10)
payment_service.set_delivery(True)
payment_service.set_strategy(PaymentByCreditCard())
payment_service.process_order()