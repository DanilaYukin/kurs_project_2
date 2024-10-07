import pytest
import requests_mock
from src.work_with_vacancies import Vacancies
from src.hh_api import GetVacanciesHH

# Мокируемый ответ от API HH.ru
MOCK_RESPONSE = {
    "items": [
        {
            "name": "Python Developer",
            "salary": {"from": 100000, "to": 150000},
            "description": "Develop Python applications",
            "url": "https://example.com/vacancy/1",
        },
        {
            "name": "Java Developer",
            "salary": {"from": 120000, "to": 180000},
            "description": "Develop Java applications",
            "url": "https://example.com/vacancy/2",
        },
    ]
}


@pytest.fixture
def mock_api():
    """Фикстура для мокирования запроса к API HH.ru."""
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json=MOCK_RESPONSE)
        yield m


def test_get_vacancies(mock_api):
    """
    Тест метода get_vacancies класса GetVacanciesHH, проверяющий, что данные с API корректно обрабатываются.
    """
    # Инициализация класса GetVacanciesHH
    parser = GetVacanciesHH("developer")

    # Вызываем метод get_vacancies и проверяем результат
    vacancies = parser.get_vacancies("developer")

    # Ожидаемый результат в формате JSON
    expected_vacancies = [
        {
            "name": "Python Developer",
            "salary": {"from": 100000, "to": 150000},
            "description": "Develop Python applications",
            "url": "https://example.com/vacancy/1",
        },
        {
            "name": "Java Developer",
            "salary": {"from": 120000, "to": 180000},
            "description": "Develop Java applications",
            "url": "https://example.com/vacancy/2",
        },
    ]

    # Преобразуем ожидания в формат JSON
    expected_json = [Vacancies(**item).to_json() for item in expected_vacancies]

    # Проверяем, что результат соответствует ожидаемому
    assert vacancies == expected_json


def test_get_vacancies_empty_response(mock_api):
    """
    Тест метода get_vacancies для обработки пустого ответа от API.
    """
    # Мокируем пустой ответ от API HH.ru
    mock_api.get("https://api.hh.ru/vacancies", json={"items": []})

    parser = GetVacanciesHH("developer")
    vacancies = parser.get_vacancies("developer")

    # Проверяем, что в случае пустого ответа метод возвращает пустой список
    assert vacancies == []
