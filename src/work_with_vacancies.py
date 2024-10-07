import json


class Vacancies:
    """Класс для работы с вакансиями"""

    name: str
    salary: int
    description: str
    url: str

    def __init__(self, name, salary, description, url):
        self.name = name
        self.salary = salary
        self.description = description
        self.url = url

        if not isinstance(self.salary, int):
            self.salary = 0

    def vacancy_salary(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f"{self.name}\nЗарплата: {self.salary}\nСсылка: {self.url}\nОписание: {self.description}\n"

    def to_json(self):
        """"""
        return self.__dict__

    @staticmethod
    def from_json(json_str):
        """
        Создает объект Vacancies из строки в формате JSON.
        """
        date = json.loads(json_str)
        return Vacancies(date["name"], date["salary"], date["description"], date["url"])
