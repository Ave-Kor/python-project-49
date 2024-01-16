# импортиурем функции из библиотеки random
from random import randint
from random import choice


# генерируем случайное число
def generate_number():
    return randint(1, 100)


# задаём вопрос (even)
def ask_even(random_number):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_number}')


# просим ввести ответ
def ask_input():
    return input('Your answer: ')


# вывод "Правильно!"
def show_correct():
    print('Correct!')


# Проверяем (even)
def check_even(user_input, random_number, name):
    if user_input.lower() == 'yes' and random_number % 2 == 0:
        show_correct()
        return True
    elif user_input.lower() == 'yes' and random_number % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print(f'''Let's try again, {name}!''')
        return False
    elif user_input.lower() == 'no' and random_number % 2 != 0:
        show_correct()
        return True
    elif user_input.lower() == 'no' and random_number % 2 == 0:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print(f'''Let's try again, {name}!''')
        return False
    else:
        print("Answer is wrong ;(. Type only 'yes' or 'no'.")
        print(f'''Let's try again, {name}!''')
        return False


# генерируем случайные числа
def generate_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer, operator = calculation(number1, number2)
    return answer, operator, number1, number2


# генерируем случайное выражение
def calculation(number1, number2):
    operators = '+-*'
    operator = choice(operators)
    if operator == '+':
        return number1 + number2, operator
    elif operator == '-':
        return number1 - number2, operator
    elif operator == '*':
        return number1 * number2, operator


# задаём вопрос (calc)
def ask_question(number1, operator, number2):
    print(f'Question: {number1} {operator} {number2}')
    u_input = int(input('Your answer: '))
    return u_input


# проверям ответ (calc, gcd)
def check_answer(u_input, answer):
    return u_input == answer


# генерируем вопрос (gcd)
def generate_question_nod():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question_string = f"Question: {number1} {number2}"
    return question_string, number1, number2, calculation_nod(number1, number2)


# считаем (gcd)
def calculation_nod(number1, number2):
    while number1 != 0 and number2 != 0:
        if abs(number1) > abs(number2):
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return abs(number1 + number2)


# задаём вопрос (gcd)
def ask_nod(number1, number2):
    print(f'Question: {number1} {number2}')
    u_input = int(input('Your answer: '))
    return u_input


# генерируем вопрос (progression)
def generate_question_prog():
    random_number = randint(1, 100)
    question_string = [random_number]
    step = randint(1, 100)
    current_number = random_number
    while len(question_string) < 10:
        current_number += step
        question_string.append(current_number)
    random_index = randint(0, len(question_string) - 1)
    answer = question_string[random_index]
    question_string[random_index] = ".."
    return question_string, answer


# задаём вопрос (progression)
def ask_prog(question_string):
    print('What number is missing in the progression?')
    question_str = ' '.join(str(num) for num in question_string)
    print('Question:', question_str)


# проверяем ответ (progression)
def check_prog(u_input, answer):
    return int(u_input) == int(answer)


# генерируем вопрос (prime)
def generate_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


# задаём вопрос (prime)
def ask_prime():
    number = generate_number()
    print('''Answer "yes" if given number is prime. Otherwise answer "no".''')
    print(f'Question: {number}')
    user_input = input('Your answer: ')
    return user_input, number


# проверяем ответ (prime)
def check_prime(user_input, number):
    if user_input.lower() == 'yes' and generate_prime(number) is True:
        return True
    elif user_input.lower() == 'no' and generate_prime(number) is False:
        return True
    else:
        return False
