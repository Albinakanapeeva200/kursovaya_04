from src.head_hunter import HeadHunterAPI
from src.super_job import SuperJobAPI
from src.json_saver import JSONSaver


def user_interaction():

    """Взаимодействие с пользователем"""

    platforms = ['1', '2']

    user_input = input('Введите платформу для поиска: 1 - HeadHunter , 2 - SuperJob \n')

    if user_input == platforms[0]:
        client = HeadHunterAPI()

        search_query = input('Вы выбрали HH ')
        hh_vacancy = client.get_vacancies(search_query)
        JSONSaver().add_vacancy(hh_vacancy)

        user_ch = input('Введите вакансию: \n')
        JSONSaver().get_info(user_ch)

        user_pick = input('Хотите отсортировать данных по З/П?: \n')

        if user_pick == 'да' or 'yes':
            JSONSaver().top_salary_vacancy(hh_vacancy)
        else:
            quit()

    elif user_input == platforms[1]:
        client = SuperJobAPI()
        search_query = input("Вы выбрали SJ ")
        sj_vacancy = client.get_vacancies(search_query)
        JSONSaver().add_vacancy(sj_vacancy)

        user_ch = input('Введите вакансию: \n')
        JSONSaver().get_info(user_ch)

        user_pick = input('Хотите отсортировать данных по З/П?: \n')

        if user_pick == 'да' or 'yes':
            JSONSaver().top_salary_vacancy(sj_vacancy)
        else:
            quit()

    elif user_input not in platforms:
        print('Такой платформы для поиска не предусмотрено')
