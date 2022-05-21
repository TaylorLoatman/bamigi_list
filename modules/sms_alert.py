from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


class SMSAlert:
    def __init__(self):
        self.sid = os.getenv("SMS_SID")
        self.token = os.getenv("SMS_TOKEN")
        self.number = os.getenv("SMS_NUM")

    def send_msg(self, name, number):
        client = Client(self.sid, self.token)
        message = client.messages.create(
            body=f"{name}, we got you all plugged in! We promise not to spam you."
                 f"Now that you're apart of the hustlers network enjoy 10% off your next purchase "
                 f"(CODE: ALLPLUGGEDIN) https://bamigishop.square.site/",
            from_=self.number,
            to=f"+1{number}"
        )
        print(message.sid)
