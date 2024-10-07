from src.utils import get_top_vacancies, sort_vacancies, sort_vacancies_by_salary, result_vacancies

# Пример тестовых данных
vacancies = [
    {
        "name": "Python Developer",
        "salary_from": 150000,
        "description": "Develop Python apps",
        "url": "https://example.com/1",
    },
    {
        "name": "Java Developer",
        "salary_from": 130000,
        "description": "Develop Java applications",
        "url": "https://example.com/2",
    },
    {
        "name": "Data Scientist",
        "salary_from": 170000,
        "description": "Work with data and ML models",
        "url": "https://example.com/3",
    },
    {
        "name": "Frontend Developer",
        "salary_from": 110000,
        "description": "Develop front-end",
        "url": "https://example.com/4",
    },
]


def test_sort_vacancies():
    result = sort_vacancies(vacancies, ["Python"])
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"

    result = sort_vacancies(vacancies, ["Python", "Java"])
    assert len(result) == 2
    assert result[0]["name"] == "Python Developer"
    assert result[1]["name"] == "Java Developer"


def test_sort_vacancies_by_salary():
    """Тест сортировки вакансий по убыванию зарплаты"""
    result = sort_vacancies_by_salary(vacancies)
    assert result[0]["salary_from"] == 170000  # Вакансия с максимальной зарплатой должна быть первой
    assert result[-1]["salary_from"] == 110000  # Вакансия с минимальной зарплатой должна быть последней


def test_get_top_vacancies():
    """Тест получения верхней части списка вакансий"""
    result = get_top_vacancies(vacancies, 2)
    assert len(result) == 2  # Проверяем, что вернулось только 2 вакансии
    assert result[0]["name"] == "Python Developer"  # Первая вакансия в списке


def test_result_vacancies(capsys):
    """Тест вывода информации о вакансиях с помощью capsys"""
    result_vacancies(vacancies)

    captured = capsys.readouterr()
    assert "Вакансия 1:" in captured.out
    assert "Python Developer" in captured.out
    assert "Зарплата от: 150000" in captured.out
    assert "https://example.com/1" in captured.out

    # Проверяем пустой список вакансий
    result_vacancies([])

    captured = capsys.readouterr()
    assert "Нет подходящих вакансий" in captured.out
