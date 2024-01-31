import random
from brain_games.constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER


GAME_QUEST = '''Answer "yes" if given number is prime. Otherwise answer "no".'''


# генерируем вопрос и ответ для prime
def question_and_answer():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = number
    if is_prime(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


# проверяем на простое число
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True
