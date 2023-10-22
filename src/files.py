import json
from os import remove
from src.data import VacancyEncoder


class FileWorker:
    """Класс для работы с файлом формата json"""
    def __init__(self):
        """Задается имя файла, можно указать путь в другую папку"""
        self.path = 'vacancies.json'

    def save_to_json(self, data):
        """Функция сохраняет переданные в неё данные в файл json"""
        try:
            with open(self.path, 'x', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=1, cls=VacancyEncoder))

        except FileExistsError:
            if input('Файл с вакансиями уже существует. Хотите перезаписать? (д/н) ') == 'д':
                with open(self.path, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(data, ensure_ascii=False, indent=1, cls=VacancyEncoder))
            else:
                pass

    def add_to_json(self, data):
        """Функция добавляет в конец файла переданные в неё данные"""
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=1))

    def del_json(self):
        """Функция удаляет существующий файл с вакансиями"""
        try:
            remove(self.path)
        except FileNotFoundError:
            print('Невозможно удалить файл так как он отсутствует')

    def get_by_salary(self, salary_from=1, salary_to=None):
        """Функция для выборки из файла по зарплате"""
        box = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                a = f.read()
                a = json.loads(a)
                for i in a:
                    if i['salary_from'] is not None and i['salary_from'] >= salary_from:
                        if salary_to is None:
                            box.append(i)
                        elif i['salary_to'] is not None and i['salary_to'] <= salary_to:
                            box.append(i)
        except FileNotFoundError:
            print('Невозможно искать в файле без самого файла')
        return box

    def count_vacancies(self):
        """Функция подсчёта количества записей в файле"""
        with open(self.path, 'r', encoding='utf-8') as f:
            a = f.read()
            a = json.loads(a)
            vacancies_counter = 0
            for _ in a:
                vacancies_counter += 1
            return vacancies_counter
