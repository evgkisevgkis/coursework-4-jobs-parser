import requests
from abc import ABC, abstractmethod


class API(ABC):
    def __init__(self, query_param=None, salary=None):
        self.vacancies = None
        self.query_param = query_param
        self.salary = salary

    @abstractmethod
    def request_vacancies(self):
        pass
