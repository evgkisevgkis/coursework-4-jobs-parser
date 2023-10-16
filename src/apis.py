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


class SuperJobAPI(API):
    """Класс для получения данных с SuperJob API"""
    def request_vacancies(self, page=0):
        header = {'X-Api-App-Id':
                  'v3.r.137892971.9bd1a19d86b81cd78d694bcd9df19f7c3ace390f.d74685e56bddcdaac706bb573ee629b35d86f2b0'}
        query_param = {'keyword': 'Python', 'page': page, 'count': 100}
        req = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=query_param)
        pages_count = round(req.json()['total'] / 100)
        while page <= pages_count:
            req = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=query_param)
            vacancies = req.json()['objects']
            for i in vacancies:
                self.vacancies.append(i)
            page += 1
        return self.vacancies
