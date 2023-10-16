import requests
from abc import ABC, abstractmethod
import json


class API(ABC):
    """Абстрактный класс для получения данных через API"""
    def __init__(self):
        self.vacancies = None

    @abstractmethod
    def request_vacancies(self):
        pass


class HeadHunterAPI(API):
    """Класс для получения данных с HH API"""
    def request_vacancies(self, page=0):
        query_param = {'text': 'NAME:Python',
                       'page': page,
                       'per_page': 100}
        req = requests.get('https://api.hh.ru/vacancies', query_param)
        return req.json()


hh = HeadHunterAPI()
print(json.dumps(hh.request_vacancies(), ensure_ascii=False, indent=1))
