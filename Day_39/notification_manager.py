from twilio.rest import Client

TWILIO_SID = "ACeImei653kMeg9g7g67GRn65z"
TWILIO_AUTH_TOKEN = "48fk1mcc8afd0v42mbvy0"
TWILIO_VIRTUAL_NUMBER = "+359887862498"
TWILIO_VERIFIED_NUMBER = "+359887862498"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)