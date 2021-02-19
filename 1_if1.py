"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должеgiн заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    age = int(input('Введите свой возраст:'))
    employment = get_employment(age)
    print('Вам {age} лет. Ваше занятие - {employment}'.format(age=age, employment=employment))


def get_employment(age):
    if age < 7:
        employment = 'Детский сад'
    elif (age > 7) and (age < 17):
        employment = 'Школа'
    elif (age > 17) and (age < 22):
        employment = 'ВУЗ'
    elif age < 120:
        employment = 'Работа'
    else: employment = 'Ваш возраст не подходит под стандарты!'
    return employment


if __name__ == "__main__":
    main()
