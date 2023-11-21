from abc import ABC, abstractmethod


class Api(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями """

    @abstractmethod
    def get_vacancies(self, job_title):
        pass


if __name__ == "__main__":
    pass
