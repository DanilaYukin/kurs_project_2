import json
from abc import ABC, abstractmethod


class Save(ABC):
    """Абстрактный класс для добавления вакансий в файл"""

    @abstractmethod
    def save_vacancies(self, vacancies):
        """Метод для добавления вакансий в файл"""

        pass

    @abstractmethod
    def get_from_file(self):
        """Метод для получения данных из файла"""

        pass

    @abstractmethod
    def delete_vacancies(self, vacancies):
        """Метод для удаления вакансий из файла"""

        pass


class VacancySave(Save):
    """Класс для добавления, удаления информации о вакансиях"""

    def __init__(self, filename="vacancies.json"):
        self.__filename = f"data/{filename}"

    def save_vacancies(self, vacancies):
        with open(self.__filename, "w") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_from_file(self):
        """Метод для получения данных из файла"""

        with open(self.__filename, "r") as file:
            return json.load(file)

    def delete_vacancies(self, vacancies):
        pass
