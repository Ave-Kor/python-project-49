from random import randint


# задаём вопрос для even
def ask_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


# генерируем вопрос и ответ для even
def question_and_answer():
    question = randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
