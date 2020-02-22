"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    w1=1
    quest = 'Как дела? '
    while w1:
        user_answer = input(quest)
        if user_answer.lower() == 'хорошо':
            w1=0
            print('Вот... сразу бы так :)')
        else:
            quest = 'А что так? Как дела? '


    
if __name__ == "__main__":
    ask_user()
