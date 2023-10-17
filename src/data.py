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
