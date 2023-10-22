from src.apis import *
import pytest


@pytest.fixture()
def return_hh():
    hh_t = HeadHunterAPI().request_vacancies()
    return hh_t


@pytest.fixture()
def return_sj():
    sj_t = SuperJobAPI().request_vacancies()
    return sj_t
