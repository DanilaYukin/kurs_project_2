def sort_vacancies(vacancies, keyword):
    """Функция для сортировки вакансий по ключевому слову"""

    return [vacancy for vacancy in vacancies if
            any(key.lower() in vacancy['description'].lower() for key in keyword)]


def sort_vacancies_by_salary(vacancies):
    """Функция для сортировки вакансий по убыванию зарплаты"""

    return sorted(
        vacancies, key=lambda vacancy: vacancy.get("salary_from" or "salary_to" or "salary", 0), reverse=True
    )


def get_top_vacancies(vacancies, top):
    """Функция для вывода верхний части списка в соответствии с указанным лимитом"""

    return vacancies[:top]


def result_vacancies(vacancies):
    """Функция для вывода  информации о вакансиях"""

    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from' or 'salary_to' or 'salary', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('url', 'Не указана')}")
    else:
        print("Нет подходящих вакансий")
