from random import randint
from random import choice


# генерируем случайное число (even)
def generate_number():
    return randint(1, 100)


# задаём вопрос (even)
def ask_even(random_number):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ', random_number)


# просим ввести ответ
def ask_input():
    return input('Your answer: ')


# вывод "Правильно!"
def show_correct():
    print('Correct!')


# Проверяем (even)
def check_even(user_input, random_number, name):
    if user_input.lower() == 'yes' and random_number % 2 == 0:
        show_correct()
        return True
    elif user_input.lower() == 'yes' and random_number % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print(f'''Let's try again, {name}!''')
        return False
    elif user_input.lower() == 'no' and random_number % 2 != 0:
        show_correct()
        return True
    elif user_input.lower() == 'no' and random_number % 2 == 0:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print(f'''Let's try again, {name}!''')
        return False
    else:
        print("Answer is wrong ;(. Type only 'yes' or 'no'.")
        print(f'''Let's try again, {name}!''')
        return False


def calculation(number1, number2):
    operators = '+-*'
    operator = choice(operators)
    if operator == '+':
        return number1 + number2, operator
    elif operator == '-':
        return number1 - number2, operator
    elif operator == '*':
        return number1 * number2, operator


def ask_question(number1, operator, number2):
    print(f'Question: {number1} {operator} {number2}')
    u_input = int(input('Your answer: '))
    return u_input


def generate_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer, operator = calculation(number1, number2)
    return answer, operator, number1, number2


def check_answer(u_input, answer):
    return u_input == answer


def generate_question_nod():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question_string = f"Question: {number1} {number2}"
    return question_string, number1, number2, calculation_nod(number1, number2)


def calculation_nod(number1, number2):
    while number1 != 0 and number2 != 0:
        if abs(number1) > abs(number2):
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return abs(number1 + number2)


def ask_nod(number1, number2):
    print(f'Question: {number1} {number2}')
    u_input = int(input('Your answer: '))
    return u_input


def check_answer_nod(u_input, answer_nod):
    return u_input == answer_nod
