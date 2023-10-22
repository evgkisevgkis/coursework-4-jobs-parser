from src.apis import *
from src.data import *
from src.files import *
from operator import itemgetter

# Получение вакансий
hh = HeadHunterAPI()
sj = SuperJobAPI()
hh_vac = hh.request_vacancies()
sj_vac = sj.request_vacancies()

# Инициализация экземпляров класса Vacancy и добавление в общий список
basket = []
for i in hh_vac:
    vaca = Vacancy(i)
    basket.append(vaca)

for v in sj_vac:
    vaca = Vacancy(v)
    basket.append(vaca)

# Сохранение списка в файл
fj = FileWorker()
fj.save_to_json(basket)
print(f"Загружено и сохранено в файл {fj.count_vacancies()} вакансий")


def user_interaction():
    """Функция для взаимодействия пользователя с сохраненными в файл данными"""
    print('Введите границы поиска по зарплате')
    salary_input_from = int(input('от '))
    try:
        salary_input_to = int(input('до(или оставьте пустым) '))
    except ValueError:
        salary_input_to = None
    filtered_vacancies = fj.get_by_salary(salary_input_from, salary_input_to)
    print(f"По запросу найдено {len(filtered_vacancies)} вакансий")
    show_amount = int(input('Сколько вакансий показать из лидеров по зарплате?'))
    filtered_vacancies.sort(key=itemgetter('salary_from'))
    for one in filtered_vacancies[0:show_amount]:
        print(one)


if __name__ == '__main__':
    user_interaction()
