class Vacancy:

    """Класс для работы с вакансиями"""

    def __init__(self, title: str, url: str, salary_from: int, salary_to, employer, req: str):
        self.title = title
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.employer = employer
        self.req = req

    def __str__(self):
        return f'{self.title}({self.url})'

    def to_dict(self):
        return {
            'Профессия': self.title,
            'Ссылка': self.url,
            'З/п от': self.salary_from,
            'З/п до': self.salary_to,
            'Работодатель': self.employer,
            'Требования': self.req

        }

    def __ge__(self, other):
        return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2

    def __le__(self, other):
        return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2

    def __eq__(self, other):
        return (self.salary_from + self.salary_to) / 2 == (other.salary_from + other.salary_to) / 2
