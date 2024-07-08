class EmailNotification:
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification:
    def send(self, message):
        print(f"Sending push notification: {message}")

class NotificationService:
    def __init__(self, notification_type):
        if notification_type == "email":
            self.notification = EmailNotification()
        elif notification_type == "sms":
            self.notification = SMSNotification()
        elif notification_type == "push":
            self.notification = PushNotification()
        else:
            raise ValueError("Unknown notification type")

    def send(self, message):
        self.notification.send(message)

# Client code
service = NotificationService("email")
service.send("Hello via Email!")

service = NotificationService("sms")
service.send("Hello via SMS!")

service = NotificationService("push")
service.send("Hello via Push Notification!")
