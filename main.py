import os

from email_sender import EmailSender
from birthday_parser import BirthParser

BASE_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    config = {
        'login': os.environ.get('LOGIN'),
        'password': os.environ.get('PASS'),
        'smtp_url': os.environ.get('SMTP_URL'),
        'smtp_port': '465',
    }
    sender = EmailSender(config)
    parser = BirthParser(f'{BASE_PATH}/data/data.csv')
    
    birthday_people = parser.get_next_week_birthdays()
    for guy in birthday_people:
        none_birthday_perss = parser.filter_none_birthday_pers(parser.data, guy)
        messages = sender.prepare_congrat_messages(none_birthday_perss, guy['name'])
        sender.send_messages(messages)
        