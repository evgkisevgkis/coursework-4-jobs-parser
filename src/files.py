import json


class FileWorker:
    """Класс для работы с файлом формата json"""
    def __init__(self):
        self.path = 'vacancies.json'

    def save_to_json(self, data):
        """Функция сохраняет переданные в неё данные в файл json"""
        with open(self.path, 'w', encoding='utf-8') as f:
            for i in data:
                f.write(json.dumps(i, ensure_ascii=False, indent=1))
