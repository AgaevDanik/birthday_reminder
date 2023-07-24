from functools import wraps
from time import sleep
from socket import gaierror
import smtplib
from typing import List, Iterable, Type
from email.message import EmailMessage
from fetchers import PersonData

"""Exceptions handler"""
def retrier(exception: Iterable[Type[Exception]]):

    def wrapper(func):

        @wraps(func)
        def inner(*args, **kwargs):
            result = None
            for time_to_wait in (1, 2, 0):
                try:
                    result = func(*args, **kwargs)
                except exception as ex:
                    print(ex)
                    sleep(time_to_wait)
                else:
                    break
            return result
        return inner
    return wrapper


class EmailSender:
    
    def __init__(self, config: dict):
        self.login = config['login']
        self.password = config['password']
        self.smtp_url = config['smtp_url']
        self.smtp_port = config['smtp_port']

    def prepare_congrat_messages(self, messages_data: Iterable[PersonData], birthday_guy_name: str) -> list:
        result = []
        for message in messages_data:

            msg = EmailMessage()
            email_to = message['email']
            msg['Subject'] = 'Birthday'
            msg['To'] = 'bmdanik1@gmail.com'
            msg['From'] = self.login
            msg.set_content(f'Hi {message["name"]}That pretty guy ({birthday_guy_name}) have birthday in 7 days')

            result.append(msg)

        return result

    @retrier((smtplib.SMTPException, gaierror))
    def send_messages(self, messages: List[EmailMessage]):
        with smtplib.SMTP_SSL(self.smtp_url, self.smtp_port) as server:

            server.login(self.login, self.password)

            for message in messages:
                server.send_message(message)
                