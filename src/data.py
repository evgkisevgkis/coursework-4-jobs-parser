import json
from typing import Any


class Vacancy:
    """Класс для вакансий"""
    def __init__(self, vac):
        """Заполнение полей данными, полученными от HH и SJ API"""
        try:
            self.name = vac['name']
            self.url = vac['alternate_url']
            try:
                self.salary_from = vac['salary']['from']
            except TypeError:
                self.salary_from = 0
            try:
                self.salary_to = vac['salary']['to']
            except TypeError:
                self.salary_to = 0
            self.experience = vac['experience']['id']
            self.description = vac['snippet']['responsibility']
        except KeyError:
            self.name = vac['profession']
            self.url = vac['link']
            self.salary_from = vac['payment_from']
            self.salary_to = vac['payment_to']
            self.experience = vac['experience']['id']
            self.description = vac['work']

    def __gt__(self, other):
        """Переопределен для возможности сравнения по зарплате"""
        return self.salary_from > other.salary_from

    def __str__(self):
        """Для строкового вывода вакансии"""
        return f"""Название вакансии: {self.name}
                   ссылка на вакансию: {self.url}
                   зарплата от: {self.salary_from}
                            до: {self.salary_to}
                   требуемый опыт: {self.experience}
                   краткое описание: {self.description}"""


class VacancyEncoder(json.JSONEncoder):
    """Класс для корректной кодировки экземпляров в JSON"""
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Vacancy):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
