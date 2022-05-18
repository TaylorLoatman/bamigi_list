import security
from twilio.rest import Client

class SMSAlert:
    def __init__(self):
        self.sid = security.sms_sid
        self.token = security.sms_token
        self.number = security.sms_number

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
