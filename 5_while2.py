"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""


questions_and_answers = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'Какой сегодня год?': '2021',
                         'Сколько тебе лет?': '30'}


def check_stop():
    signal = False
    stop_answer = input('Продолжим? Ответьте Да или Нет')
    if stop_answer == 'Да':
        signal = False
    elif stop_answer == 'Нет':
        signal = True
    else:
        print('Я не понимаю ваш ответ')
        check_stop()
    return signal


def ask_user(answers_dict):
    stop = False
    while not stop:
        user_answer = input('Введите ваш вопрос: ')
        if user_answer in answers_dict.keys():
            print(f'Программа: {answers_dict[user_answer]}')
            stop = check_stop()
        else:
            print('Программа: К сожалению ваш вопрос мне непонятен')
            stop = check_stop()


if __name__ == "__main__":
    ask_user(questions_and_answers)
