"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def set_query(string):
    """Функция ставит знак вопроса (?) в конец строки если его там нет"""
    if string.endswith('?'):
        return string
    else:
        return string.ljust(len(string) + 1, '?')


def ask_user():
    """
    Замените pass на ваш код
    """
    dict1 = {"как дела?": "Хорошо!", "что делаешь?": "Программирую", "как здоровье?": "Отлично!",
             "как погода?": "Лучше не бывает :)", "на выход?": "Как скажешь ;)"}
    w1 = 1
    quest = 'Задайте вопрос: '
    while w1:
        try:
            user_answer = set_query(input(quest).lower())
            if user_answer in dict1:
                print(dict1[user_answer])
                """Выход по ввводу этой фразы"""
                if user_answer == "на выход?":
                    w1 = 0
            else:
                print('Всё нормуль :)')
        except KeyboardInterrupt:
            print('')
            print('Пока!')
            w1=0

if __name__ == "__main__":
    ask_user()
