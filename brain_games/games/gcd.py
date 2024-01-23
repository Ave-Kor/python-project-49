import random


# задаём вопрос для gcd
def ask_question():
    print('Find the greatest common divisor of given numbers.')


# генерируем вопрос и ответ для gcd
def question_and_answer():
    number1, number2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{number1} {number2}'

    def calculate_gcd(number1, number2):
        while number1 != 0 and number2 != 0:
            if abs(number1) > abs(number2):
                number1 %= number2
            else:
                number2 %= number1
        return number1 or number2
    answer = calculate_gcd(number1, number2)
    return (question, answer)
