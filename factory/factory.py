from abc import ABC, abstractmethod

# Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        raise NotImplementedError("You should implement this method.")

# Concrete Product 1
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending email: {message}")

# Concrete Product 2
class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

# Concrete Product 3
class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending push notification: {message}")

# Factory Interface
class NotificationFactory:
    @abstractmethod
    def create_service(self) -> Notification:
        pass

# Concrete Factory 1      
class EmailNotificationFactory(NotificationFactory):
    def create_service(self) -> Notification:
        print("Creating Email Notification Service!")
        notification: Notification = EmailNotification()
        return notification

# Concrete Factory 2 
class SMSNotificationFactory(NotificationFactory):
    def create_service(self) -> Notification:
        print("Creating SMS Notification Service!")
        notification: Notification = SMSNotification()
        return notification

# Concrete Factory 3  
class PushNotificationFactory(NotificationFactory):
    def create_service(self) -> Notification:
        print("Creating Push Notification Service!")
        notification: Notification = PushNotification()
        return notification

if __name__ == "__main__":
    sms_factory = SMSNotificationFactory()
    sms_notification = sms_factory.create_service()
    sms_notification.send("Hello")

