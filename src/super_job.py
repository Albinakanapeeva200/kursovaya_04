import requests
from src.vacancy import Vacancy
from src.api import Api


class SuperJobAPI(Api):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):

        """Запрос к API SJ"""

        params = {'count': 50,
                  'town': 0,
                  'keyword': job_title
                  }
        super_job_api = 'v3.r.137575001.25e7b42b93e4624890e7bdde41d586b710997eb3.' \
                        '4e28b814a6d6f7ea4e9415050236c7948508cf49'
        headers = {'X-Api-App-Id': super_job_api}
        req = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        return self.vacancies_pars(req.json())

    def vacancies_pars(self, js_obj):

        """Парсинг полученных вакансий"""

        all_vacancy = []
        for obj in js_obj['objects']:
            all_vacancy.append(Vacancy(**{
                'title': obj['profession'],
                'salary_from': obj['payment_from'],
                'salary_to': obj['payment_to'],
                'employer': obj['firm_name'],
                'url': obj['link'],
                'req': obj['candidat']
            }))
        return all_vacancy


if __name__ == "__main__":
    pass
