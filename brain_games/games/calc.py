import random
from brain_games.constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER


GAME_QUEST = 'What is the result of the expression?'


# генерируем вопрос и ответ для clac
def question_and_answer():
    """Brain-calc

    Цель игры: пользователю показывается случайное
    математическое выражение,например 35 + 16, которое нужно
    вычислить и записать правильный ответ

    """
    number1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operators = '+-*'
    operator = random.choice(operators)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        answer = number1 + number2
    if operator == '-':
        answer = number1 - number2
    if operator == '*':
        answer = number1 * number2
    return question, answer
