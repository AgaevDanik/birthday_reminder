from abc import ABC, abstractmethod
from typing import List, TypedDict

PersonData = TypedDict("PersonData", {"name": str, "email": str, "birth_date": str})

"""Strategy OOP pattern"""
class FetchStrategy(ABC):

    @classmethod
    @abstractmethod
    def init_data(cls, path: str) -> List[PersonData]:
        raise NotImplementedError()