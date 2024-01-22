from random import randint, choice


# задаём вопрос для calc
def ask_question():
    print('What is the result of the expression?')


# генерируем вопрос и ответ для clac
def question_and_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operators = '+-*'
    operator = choice(operators)
    question = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    if operator == '-':
        answer = number1 - number2
    if operator == '*':
        answer = number1 * number2
    return question, answer
