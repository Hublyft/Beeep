
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import os


class CloudMessaging:
    def __init__(self):
        base_path = "E:\Documents\python projects\django projects"
        path = os.path.join(
            base_path, "beeep-69bdd-firebase-adminsdk-r65i8-8b608b84ea.json")
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

    @staticmethod
    def send_broadcast_to_lawyers(tokens, name):
        # See documentation on defining a message payload.
        message = messaging.Message(
            notification=messaging.Notification(
                title="Beeep Alert",
                body="Beeep alert sent from {}".format(name)
            ),
            token=tokens,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)

    @staticmethod
    def send_beep_to_buddy(token,name):
        message = messaging.Message(
            notification=messaging.Notification(
                title="Beeep Alert",
                body="Beeep alert sent from {}".format(name)
            ),
            data={"name":name},
            token=token,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
