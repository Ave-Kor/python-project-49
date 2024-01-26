import random


GAME_QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


# генерируем вопрос и ответ для even
def question_and_answer():
    question = random.randint(1, 100)
    if is_even(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


# проверяем even
def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False
