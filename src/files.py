import json
from os import remove


class FileWorker:
    """Класс для работы с файлом формата json"""
    def __init__(self):
        self.path = 'vacancies.json'

    def save_to_json(self, data):
        """Функция сохраняет переданные в неё данные в файл json"""
        try:
            with open(self.path, 'x', encoding='utf-8') as f:
                for i in data:
                    f.write(json.dumps(i, ensure_ascii=False, indent=1))
        except FileExistsError:
            if input('Файл с вакансиями уже существует. Хотите перезаписать? (д/н) ') == 'д':
                with open(self.path, 'w', encoding='utf-8') as f:
                    for i in data:
                        f.write(json.dumps(i, ensure_ascii=False, indent=1))
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

