from src.hh_api import GetVacanciesHH
from src.save_vacancies import VacancySave
from src.utils import sort_vacancies, sort_vacancies_by_salary, result_vacancies, get_top_vacancies


def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_api = GetVacanciesHH()
    hh_vacancies = hh_api.get_vacancies(search_query)
    save_vacancy = VacancySave()
    save_vacancy.save_vacancies(hh_vacancies)
    print("Ответ API:", hh_vacancies)

    if hh_vacancies:
        vacancies_list = []

        for vacancy in hh_vacancies:
            print(vacancy)
            vacancies_list.append(vacancy)

        print(vacancies_list)
        filtered_vacancies = sort_vacancies(vacancies_list, filter_words)
        sorted_vacancies_salary = sort_vacancies_by_salary(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies_salary, top_n)
        result_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")
