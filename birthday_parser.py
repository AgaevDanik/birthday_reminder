from fetchers.csv_fetcher import FetchCSV, PersonData
import datetime as dt
from typing import List
from validation import PersonDataValidator


class BirthParser:

    strategy_map = {
        'csv': FetchCSV,
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.fetch_manager = self._get_strategy()
        try:
            self.data = self.fetch_manager.init_data(file_path)
        except (OSError, FileNotFoundError):
            raise RuntimeError(f'There is wrong file path {file_path}')
        
    @staticmethod
    def filter_none_birthday_pers(pers_data, birthday_pers):
        return filter(lambda pers: pers['email'] != birthday_pers['email'], pers_data)

        

    def _get_strategy(self):
        return self.strategy_map[self.file_path.split('.')[-1]]
    
    @staticmethod
    def _get_next_week_date() -> dt.date:    
        next_week_datetime = dt.datetime.today() + dt.timedelta(days=7)
        return next_week_datetime.date()


    def get_next_week_birthdays(self) -> List[PersonData]:
        result = []
        next_week_date = self._get_next_week_date()
        for person in self.data:
            birth_date = person['birth_date']
            date_format = PersonDataValidator.get_date_format(birth_date)

            if birth_date[5:] == next_week_date.strftime('%m-%d'):
                result.append(person)
                
        return result
    