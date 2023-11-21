import json


class JSONSaver:

    """Класс для сохранения полученных вакансий файл,
    а так же получения информации о вакансии, её удалении и сортировке"""

    @staticmethod
    def add_vacancy(obj):
        file = open('vacancy.json', mode='w', encoding='utf8')
        _list = [v.to_dict() for v in obj]
        file.write(json.dumps(_list, ensure_ascii=False, indent=2))
        file.close()

    @staticmethod
    def remove_vacancy(vacancy_del):

        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            for v in obj:
                if v['Профессия'] == vacancy_del:
                    obj.remove(v)
            with open('vacancy.json', mode='w', encoding='utf8') as out_file:
                json.dump(obj, out_file, ensure_ascii=False, indent=2)
            out_file.close()

    @staticmethod
    def get_info(vacancy):
        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            for v in obj:
                try:
                    if vacancy in v['Профессия']:
                        print(v)
                except Exception:
                    raise Exception("Извините вакансия не найдена =(")

    @staticmethod
    def top_salary_vacancy(obj):
        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            object_ = sorted(obj, key=lambda salary: salary['З/п до'])
            print(object_)


if __name__ == '__main__':
    pass
