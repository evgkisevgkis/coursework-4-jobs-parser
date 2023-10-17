class Vacancy:
    """Класс для вакансий"""
    def __init__(self, vac):
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
        return self.salary_from > other.salary_from

    def __str__(self):
        return f"""Название вакансии: {self.name}
                   ссылка на вакансию: {self.url}
                   зарплата от: {self.salary_from}
                            до: {self.salary_to}
                   требуемый опыт: {self.experience}
                   краткое описание: {self.description}"""
