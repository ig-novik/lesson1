"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def  list_avg(list):
    list_sum = 0
    for m in list:
        list_sum += m
    return list_sum/len(list)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '4б', 'scores': [5,4,3,2,5]},
        {'school_class': '4в', 'scores': [4,5,3,4,5]},
        {'school_class': '4г', 'scores': [2,5,4,5,3]}
    ]
    all=[]
    for i in scores:
        print('средняя оценка по классу ' + i['school_class'] + ' - ' + str(list_avg(i['scores'])))
        for j in i['scores']:
            all.append(j)
    print('средняя оценка по школе ' + '    - ' + str(list_avg(all)))



    
if __name__ == "__main__":
    main()
