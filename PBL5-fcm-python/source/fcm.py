import firebase_admin
from firebase_admin import credentials, messaging


cred = credentials.Certificate("source/secret/firebase_secret.json")

def send_message(token, title, body):
    firebase_admin.initialize_app(cred)
    messaging = firebase_admin.messaging
    message = messaging.Message(
        data={
            "title": title,
            "body": body
        },
        token=token,
        notification=messaging.Notification(title=title, body=body)
    )
    response = messaging.send(message)
    return response



send_message("d8cZzc9XTj-83PUyeSsxEy:APA91bGRCTCIMjqWKQ8BP3tkJZ6Femr1sT9GdiceWeQkXkQXxuZOqpOTL4xti5BiKEzjuuZoNc8I8Y2wBk-uuuVxWOI49tCAP5UmYeqbngm18NX46FesTlo", "title", "body")