import pytest
import json
import os
from src.save_vacancies import VacancySave


@pytest.fixture
def test_vacancies():
    """Фикстура с тестовыми данными о вакансиях"""
    return [
        {
            "name": "Python Developer",
            "salary": 150000,
            "description": "Develop Python applications",
            "url": "http://example.com",
        },
        {
            "name": "Java Developer",
            "salary": 130000,
            "description": "Develop Java applications",
            "url": "http://example2.com",
        },
    ]


def test_save_vacancies(tmpdir, test_vacancies):
    """Тест метода save_vacancies на корректное сохранение данных в файл"""
    # Создаем временный файл
    temp_file = tmpdir.join("vacancy.json")

    # Инициализируем класс VacancySave с временным файлом
    vacancy_save = VacancySave(temp_file)

    # Сохраняем вакансии в файл
    vacancy_save.save_vacancies(test_vacancies)

    # Проверяем, что файл был создан
    assert os.path.exists(temp_file)

    # Проверяем содержимое файла
    with open(temp_file, "r") as f:
        data = json.load(f)

    assert data == test_vacancies


def test_get_from_file(tmpdir, test_vacancies):
    """Тест метода get_from_file на корректное чтение данных из файла"""
    # Создаем временный файл и записываем туда тестовые вакансии
    temp_file = tmpdir.join("vacancy.json")
    with open(temp_file, "w") as f:
        json.dump(test_vacancies, f, ensure_ascii=False, indent=4)

    # Инициализируем класс VacancySave с временным файлом
    vacancy_save = VacancySave(temp_file)

    # Получаем данные из файла
    loaded_vacancies = vacancy_save.get_from_file()

    # Проверяем, что данные совпадают
    assert loaded_vacancies == test_vacancies


def test_get_from_empty_file(tmpdir):
    """Тест метода get_from_file на обработку пустого файла"""
    # Создаем пустой временный файл
    temp_file = tmpdir.join("vacancy.json")
    temp_file.write("[]")  # Пустой массив JSON

    # Инициализируем класс VacancySave с временным файлом
    vacancy_save = VacancySave(temp_file)

    # Получаем данные из файла
    loaded_vacancies = vacancy_save.get_from_file()

    # Проверяем, что данные пустые
    assert loaded_vacancies == []


def test_file_not_found(tmpdir):
    """Тест метода get_from_file на обработку несуществующего файла"""
    temp_file = tmpdir.join("non_existent.json")

    # Инициализируем класс VacancySave с файлом, которого нет
    vacancy_save = VacancySave(temp_file)

    # Проверяем, что при попытке прочитать несуществующий файл возникает ошибка
    with pytest.raises(FileNotFoundError):
        vacancy_save.get_from_file()
