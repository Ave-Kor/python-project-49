from random import randint
from random import choice


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
