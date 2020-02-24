"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    quest = 'Как дела? '
    while True:
        user_answer = input(quest)
        if user_answer.lower() == 'хорошо':
            print('Замечательно! Пока.прор')
            break
        else:
            quest = 'А что так? Как дела? '


    
if __name__ == "__main__":
    ask_user()
