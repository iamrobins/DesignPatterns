from abc import ABC, abstractmethod

# The base Notifier interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# Concrete implementation of the base notifier
class BaseNotifierEmail(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending Email: {message}")

# Base Decorator class implementing the Notifier interface
class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier) -> None:
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)

# Concrete Decorator for WhatsApp notifications
class WhatsAppNotifier(NotifierDecorator):
    # No explicit constructor, so it uses the constructor of NotifierDecorator
    def send(self, message: str) -> None:
        super().send(message)  # Calls NotifierDecorator's send method
        print(f"Sending WhatsApp Message: {message}")

# Concrete Decorator for SMS notifications
class SMSNotifier(NotifierDecorator):
    # No explicit constructor, so it uses the constructor of NotifierDecorator
    def send(self, message: str) -> None:
        super().send(message)  # Calls NotifierDecorator's send method
        print(f"Sending SMS: {message}")

# Client code
if __name__ == "__main__":
    # Create a base notifier
    email_notifier = BaseNotifierEmail()

    # Decorate it with WhatsAppNotifier
    whatsapp_notifier = WhatsAppNotifier(email_notifier)

    # Further decorate it with SMSNotifier
    sms_notifier = SMSNotifier(whatsapp_notifier)

    # Send a message using the decorated notifier
    sms_notifier.send("Hello, this is a test message!")
