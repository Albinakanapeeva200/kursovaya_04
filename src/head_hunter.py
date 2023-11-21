import requests
import json
from src.api import Api


class HeadHunterAPI(Api):

    def __init__(self):
        pass

    def get_vacancies(self, keyword):
        """Запрос к API HH"""

        params = {
            'text': keyword,
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
            salary = obj.get('salary') or {}
            all_vacancy.append(Vacancy(**{
                'name': obj['name'],
                'salary_from': salary.get('from', 0),
                'salary_to': salary.get('to', 0),
                'company': obj['company']['name'],
                'url': obj['url'],
                'description': obj['snippet']['description']
            }))

        return all_vacancy


if __name__ == "__main__":
    pass
