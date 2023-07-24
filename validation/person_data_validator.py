from datetime import datetime as dt
from abc import ABC, abstractmethod

from fetchers import PersonData


class AbstractValidator(ABC):

    @classmethod
    @abstractmethod
    def validate(cls, data: PersonData):
        raise NotImplementedError()

class PersonDataValidator(AbstractValidator):

    @classmethod
    def validate(cls, data: PersonData):
        cls.validate_date(data.get('birth_date', ''))
        cls.validate_email(data.get('email', ''))
        cls.validate_name(data.get('name', ''))
    
    @staticmethod
    def get_date_format(date: str) -> str:
        date_format = '%Y-%m-%d'
        if len(date) == 5:
            date_format = '%m-%d'
        return date_format
        
    @classmethod
    def validate_date(cls, date: str):
        date_format = cls.get_date_format(date)

        try:
            birth_date = dt.strptime(date, date_format).date()
        except (ValueError, TypeError):
            print(f'Date {date} is not valid')
            exit()

        if dt.today().date() < birth_date:
            print(f'Date {date} is in the past')
            exit()

    @staticmethod
    def validate_email(email: str):

        if not email.strip():
            print('Data is not valid some email is empty')

    @staticmethod
    def validate_name(name: str):
        if not name.strip():
            print('Data is not valid some name is empty')
