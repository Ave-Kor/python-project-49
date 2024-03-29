import random
from brain_games.constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER


GAME_QUEST = 'Find the greatest common divisor of given numbers.'


# генерируем вопрос и ответ для gcd
def question_and_answer():
    """Game-gcd

    Цель игры: пользователю показывается два случайных числа,
    например, 25 50. Пользователь должен вычислить и ввести наибольший
    общий делитель этих чисел

    """
    number1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'{number1} {number2}'
    calculate_gcd(number1, number2)
    answer = calculate_gcd(number1, number2)
    return (question, answer)


# рассчитываем наибольший общий делитель
def calculate_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if abs(number1) > abs(number2):
            number1 %= number2
        else:
            number2 %= number1
    return number1 or number2
