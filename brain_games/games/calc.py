import random


GAME_QUEST = 'What is the result of the expression?'


# генерируем вопрос и ответ для clac
def question_and_answer():
    number1, number2 = random.randint(1, 100), random.randint(1, 100)
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
