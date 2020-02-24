"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def list_avg(lst):
    return sum(lst) / len(lst)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_data = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '4б', 'scores': [5, 4, 3, 2, 5]},
        {'school_class': '4в', 'scores': [4, 5, 3, 4, 5]},
        {'school_class': '4г', 'scores': [2, 5, 4, 5, 3]}
    ]
    school_scores = []
    for classes in school_data:
        print('средняя оценка по классу ' + classes['school_class'] + ' - ' + str(list_avg(classes['scores'])))
        school_scores.extend(classes['scores'])
    print('средняя оценка по школе ' + '    - ' + str(list_avg(school_scores)))


if __name__ == "__main__":
    main()
