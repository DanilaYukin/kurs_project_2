from abc import ABC, abstractmethod

import requests

from src.work_with_vacancies import Vacancies


class Parser(ABC):
    """Абстрактный класс для работы по поиску вакансий с сайта HH.ru"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод для получения вакансий по ключевому слову"""
        pass


class GetVacanciesHH(Parser):
    """
    Класс для работы с API
    Класс Parser является родительским классом
    """

    def __init__(self, file_worker: str):
        self.url = "https://api.hh.ru/vacancies"
        self.__params = {f"text: {file_worker}"}
        self.vacancies = []

    def get_vacancies(self, keyword: str):
        """Метод для получения вакансий по ключевому слову"""

        response = requests.get(self.url, params=self.__params).json()['items']
        for vacancies in response:
            name = vacancies.get("name", "Не указано")
            salary = vacancies.get("salary" or "salary_from" or "salary_to")
            description = vacancies.get("description", "Не указано")
            url = vacancies.get("url", "Не указано")
            self.vacancies.append(Vacancies(name, salary, description, url).to_json())
            return self.vacancies
