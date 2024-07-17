from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List

class Event(Enum):
    NEW_ITEM = "NEW_ITEM"
    SALE = "SALE"

# Subscriber
class EventListener(ABC):
    @abstractmethod
    def update(self, event_type: Event) -> None:
        pass

class EmailListener(EventListener):
    def __init__(self, email: str) -> None:
        self.email = email
    
    def update(self, event_type: Event) -> None:
        print(f"Sending email notification about {event_type.value} to {self.email}")

class AppListener(EventListener):
    def __init__(self, username: str) -> None:
        self.username = username

    def update(self, event_type: Event) -> None:
        print(f"Sending app notification about {event_type.value} to {self.username}")

# Publisher
class NotificationService:
    def __init__(self) -> None:
        self.customers: Dict[str, List[EventListener]] = {event.value: [] for event in Event}

    def subscribe(self, event_type: Event, listener: EventListener) -> None:
        self.customers[event_type.value].append(listener)
    
    def unsubscribe(self, event_type: Event, listener: EventListener) -> None:
        self.customers[event_type.value].remove(listener)

    def notify(self, event_type: Event) -> None:
        for listener in self.customers[event_type.value]:
            listener.update(event_type)

# Creating instances of NotificationService and listeners
notification_service = NotificationService()
alex_email_user = EmailListener("alex@example.com")
john_email_user = EmailListener("john@example.com")
peter_app_user = AppListener("peter")
william_app_user = AppListener("william")

# Subscribing listeners to events
notification_service.subscribe(Event.NEW_ITEM, alex_email_user)
notification_service.subscribe(Event.NEW_ITEM, john_email_user)
notification_service.subscribe(Event.NEW_ITEM, peter_app_user)
notification_service.subscribe(Event.SALE, william_app_user)

# Notifying listeners of a new item
notification_service.notify(Event.NEW_ITEM)

# Unsubscribing a listener and notifying again
notification_service.unsubscribe(Event.NEW_ITEM, john_email_user)
print("AFTER REMOVING A USER")
notification_service.notify(Event.NEW_ITEM)

# Notifying listeners of a sale
print("ONLY NOTIFYING SALES NOW")
notification_service.notify(Event.SALE)
