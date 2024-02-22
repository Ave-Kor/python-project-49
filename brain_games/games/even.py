import random
from brain_games.constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER


GAME_QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


# генерируем вопрос и ответ для even
def question_and_answer():
    """Brain-even

    Цель игры: пользователь должен ответить "yes", если число на экране
    - чётное. В противном случае следует ответить "no".

    """
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
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
