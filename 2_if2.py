"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def checker_string(str1, str2):
    if isinstance(str1, str) and isinstance(str1, str):
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
        else:
            return 'Нет значения для такого набора'
    else:
        return 0


def main():
    print(checker_string('MYA', 'MYA'))
    print(checker_string('MYA1', 'MYA'))
    print(checker_string('MYA1', 'MYA2'))
    print(checker_string('MYA1', 'learn'))
    print(checker_string(1, 2))


    
if __name__ == "__main__":
    main()
