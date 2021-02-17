"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


school_statistics = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                     {'school_class': '4b', 'scores': [1, 3, 4, 5, 5]},
                     {'school_class': '4c', 'scores': [3, 3, 3, 4, 5, 2, 3]},
                     {'school_class': '11a', 'scores': [3, 4, 4, 5, 5]}]


def main():
    all_scores = []
    for el in school_statistics:
        el['avg'] = sum(el['scores']) / len(el['scores'])
        all_scores.append(el['avg'])
        print(f'Для класса {el["school_class"]} среднее значение - {el["avg"]}')
    school_avg = sum(all_scores) / len(all_scores)
    print(f"Средний балл по школе: {school_avg}")
    
if __name__ == "__main__":
    main()
