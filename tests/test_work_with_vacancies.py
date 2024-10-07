import json

from src.work_with_vacancies import Vacancies


def test_vacancies_initialization():
    """
    Тестирует инициализацию объекта Vacancies и правильность присваивания значений.
    """
    vacancy = Vacancies("Developer", 100000, "Python developer", "http://example.com")

    assert vacancy.name == "Developer"
    assert vacancy.salary == 100000
    assert vacancy.description == "Python developer"
    assert vacancy.url == "http://example.com"


def test_vacancies_salary_default():
    """
    Проверяет, что если salary не является целым числом, то устанавливается значение 0.
    """
    vacancy = Vacancies("Developer", "not a number", "Python developer", "http://example.com")

    assert vacancy.salary == 0


def test_vacancy_salary_comparison():
    """
    Тестирует метод vacancy_salary для сравнения зарплат.
    """
    vacancy1 = Vacancies("Developer", 100000, "Python developer", "http://example.com")
    vacancy2 = Vacancies("Manager", 150000, "Management position", "http://example2.com")

    assert vacancy1.vacancy_salary(vacancy2) is True  # У первой вакансии зарплата меньше
    assert vacancy2.vacancy_salary(vacancy1) is False  # У второй вакансии зарплата больше


def test_vacancies_to_json():
    """
    Тестирует преобразование объекта Vacancies в формат JSON.
    """
    vacancy = Vacancies("Developer", 100000, "Python developer required", "http://example.com")

    expected_json = {
        "name": "Developer",
        "salary": 100000,
        "description": "Python developer required",
        "url": "http://example.com",
    }

    assert vacancy.to_json() == expected_json


def test_vacancies_from_json():
    """
    Тестирует создание объекта Vacancies из JSON строки.
    """
    json_str = json.dumps(
        {"name": "Developer", "salary": 100000, "description": "Python developer", "url": "http://example.com"}
    )

    vacancy = Vacancies.from_json(json_str)

    assert vacancy.name == "Developer"
    assert vacancy.salary == 100000
    assert vacancy.description == "Python developer"
    assert vacancy.url == "http://example.com"


def test_vacancies_str():
    """
    Тестирует строковое представление объекта Vacancies.
    """
    vacancy = Vacancies("Developer", 100000, "Python developer required", "http://example.com")

    expected_str = (
        "Developer\n" "Зарплата: 100000\n" "Ссылка: http://example.com\n" "Описание: Python developer required\n"
    )

    assert str(vacancy) == expected_str
