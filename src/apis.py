import requests
from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный класс для получения данных через API"""
    def __init__(self):
        self.vacancies = []

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
        pages_count = req.json()['pages']
        while page <= pages_count:
            req = requests.get('https://api.hh.ru/vacancies', query_param)
            vacancies = req.json()['items']
            for i in vacancies:
                self.vacancies.append(i)
            page += 1
        return self.vacancies
