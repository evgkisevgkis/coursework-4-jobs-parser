from pytest import raises
from src.data import *


def test_vacancy():
    with raises(TypeError):
        _ = Vacancy()


def test_vacancy_2(return_hh):
    a = Vacancy(return_hh[0])
    assert a.__class__ == Vacancy
