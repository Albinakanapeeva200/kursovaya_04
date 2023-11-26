import requests
import json
from src.api import Api
from src.vacancy import Vacancy


class HeadHunterAPI(Api):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        """Запрос к API HH"""

        params = {
            'text': job_title,
            'area': 1,
            'page': 0,
            'per_page': 50
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        js_obj = json.loads(data)
        return self.vacancies_pars(js_obj)

    def vacancies_pars(self, js_obj):
        """Парсинг полученных вакансий"""

        all_vacancy = []
        for obj in js_obj['items']:
            if not obj['salary']['from'] or not obj['salary']['to']:
                continue
            else:
                salary = obj.get('salary')
                all_vacancy.append(Vacancy(**{
                    'title': obj['name'],
                    'salary_from': salary.get('from', 0),
                    'salary_to': salary.get('to', 0),
                    'employer': obj['employer']['name'],
                    'url': obj['url'],
                    'req': obj['snippet']['requirement']
                }))

            return all_vacancy


if __name__ == "__main__":
    pass
