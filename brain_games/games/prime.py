import random


GAME_QUEST = '''Answer "yes" if given number is prime. Otherwise answer "no".'''


# генерируем вопрос и ответ для prime
def question_and_answer():
    number = random.randint(1, 100)
    question = number
    if is_prime(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False

    return True
