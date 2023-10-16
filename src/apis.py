import requests
from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный класс для получения данных через API"""
    def __init__(self):
        self.vacancies = None
        self.query_param = None
        self.salary = None
        self.url = None
        self.req = requests.get(self.url, self.query_param)

    @abstractmethod
    def request_vacancies(self):
        pass
