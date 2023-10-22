from src.files import *


def test_file_worker():
    fw = FileWorker()
    # fw.path = '../vacancies.json'
    t_b = fw.get_by_salary()
    assert t_b[0].__class__ == dict
