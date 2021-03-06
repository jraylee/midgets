from my_midgets.midget import Midget
from my_midgets.password_config import GMAIL_PASSWORD
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PingMidget(Midget):

    ACCOUNT = "midgetping@gmail.com"

    def __init__(self):
        super().__init__()

    def ping(self, to, message=None):
        msg = MIMEMultipart()
        msg["From"] = self.ACCOUNT
        msg["To"] = to
        msg["Subject"] = "Ping!"

        html = '<html><body><p>Hi, I have the following alerts for you!</p><h1>{}</h1></body></html>'.format(message if message is not None else "")
        body = MIMEText(html, 'html')

        msg.attach(body)
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        s.login(self.ACCOUNT, GMAIL_PASSWORD)
        s.sendmail(self.ACCOUNT, to, msg.as_string())

if __name__ == "__main__":
    pinger = PingMidget()
    pinger.ping("TEST@gmail.com")
