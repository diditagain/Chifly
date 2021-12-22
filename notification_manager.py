import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    to_mail = os.getenv("TO_EMAIL")

    def __init__(self) -> None:
        pass

    def send_mail(self, message):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.to_mail,
                msg=f"Subject:Cheap Flight Alert! \n\n {message}"
            )
        
