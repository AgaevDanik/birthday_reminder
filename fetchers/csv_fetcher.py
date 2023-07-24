import csv

from typing import List
from . import PersonData, FetchStrategy
from validation import PersonDataValidator


class FetchCSV(FetchStrategy):
    @classmethod
    def init_data(cls, path: str) -> List[PersonData]:
        data: List[PersonData] = []
        with open(path, newline="") as csv_file:
            reader = csv.reader(csv_file)

            for index, row in enumerate(reader):
                if index == 0:
                    continue
                if len(row) != 3:
                    print(f"Row number {index + 1}, has elements qty != 3")
                    continue

                email, name, birth_date = row

                person_data: PersonData = {
                    "name": name,
                    "email": email,
                    "birth_date": birth_date,
                }
                
                PersonDataValidator.validate(person_data)

                data.append(person_data)

        return data
