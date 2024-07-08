from abc import ABC, abstractmethod

# Abstract Product Interfaces
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class AdvancedNotification(ABC):
    @abstractmethod
    def send_with_priority(self, message: str, priority: int):
        pass

# Concrete Product Classes
class SimpleEmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending simple email: {message}")

class SimpleSMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending simple SMS: {message}")

class SimplePushNotification(Notification):
    def send(self, message: str):
        print(f"Sending simple push notification: {message}")

class SimplePopupNotification(Notification):
    def send(self, message: str):
        print(f"Displaying simple popup notification: {message}")

class AdvancedEmailNotification(AdvancedNotification):
    def send_with_priority(self, message: str, priority: int):
        print(f"Sending advanced email with priority {priority}: {message}")

class AdvancedSMSNotification(AdvancedNotification):
    def send_with_priority(self, message: str, priority: int):
        print(f"Sending advanced SMS with priority {priority}: {message}")

class AdvancedPushNotification(AdvancedNotification):
    def send_with_priority(self, message: str, priority: int):
        print(f"Sending advanced push notification with priority {priority}: {message}")

class AdvancedPopupNotification(AdvancedNotification):
    def send_with_priority(self, message: str, priority: int):
        print(f"Displaying advanced popup notification with priority {priority}: {message}")

# Abstract Factory Interface
class NotificationFactory(ABC):
    @abstractmethod
    def create_email_notification(self) -> Notification:
        pass

    @abstractmethod
    def create_sms_notification(self) -> Notification:
        pass

    @abstractmethod
    def create_push_notification(self) -> Notification:
        pass

    @abstractmethod
    def create_popup_notification(self) -> Notification:
        pass

# Concrete Factory Classes for Simple Notifications
class SimpleNotificationFactory(NotificationFactory):
    def create_email_notification(self) -> Notification:
        return SimpleEmailNotification()

    def create_sms_notification(self) -> Notification:
        return SimpleSMSNotification()

    def create_push_notification(self) -> Notification:
        return SimplePushNotification()

    def create_popup_notification(self) -> Notification:
        return SimplePopupNotification()

# Concrete Factory Classes for Advanced Notifications
class AdvancedNotificationFactory(NotificationFactory):
    def create_email_notification(self) -> AdvancedNotification:
        return AdvancedEmailNotification()

    def create_sms_notification(self) -> AdvancedNotification:
        return AdvancedSMSNotification()

    def create_push_notification(self) -> AdvancedNotification:
        return AdvancedPushNotification()

    def create_popup_notification(self) -> AdvancedNotification:
        return AdvancedPopupNotification()

# Client code
if __name__ == "__main__":
    # Using Simple Notification Factory
    simple_factory = SimpleNotificationFactory()
    
    simple_email = simple_factory.create_email_notification()
    simple_email.send("Simple Email Message")
    
    simple_sms = simple_factory.create_sms_notification()
    simple_sms.send("Simple SMS Message")
    
    simple_push = simple_factory.create_push_notification()
    simple_push.send("Simple Push Message")
    
    simple_popup = simple_factory.create_popup_notification()
    simple_popup.send("Simple Popup Message")

    # Using Advanced Notification Factory
    advanced_factory = AdvancedNotificationFactory()
    
    advanced_email = advanced_factory.create_email_notification()
    advanced_email.send_with_priority("Advanced Email Message", 1)
    
    advanced_sms = advanced_factory.create_sms_notification()
    advanced_sms.send_with_priority("Advanced SMS Message", 2)
    
    advanced_push = advanced_factory.create_push_notification()
    advanced_push.send_with_priority("Advanced Push Message", 3)
    
    advanced_popup = advanced_factory.create_popup_notification()
    advanced_popup.send_with_priority("Advanced Popup Message", 4)
