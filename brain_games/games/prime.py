from random import randint


# задаём вопрос для prime
def ask_question():
    print('''Answer "yes" if given number is prime. Otherwise answer "no".''')


# генерируем вопрос и ответ для prime
def question_and_answer():
    number = randint(1, 100)
    question = number
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            answer = 'no'
        else:
            answer = 'yes'
    return question, answer
