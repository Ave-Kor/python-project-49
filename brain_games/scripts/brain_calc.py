from random import randint
from random import choice
from brain_games.cli import welcome_user


def calculation(number1, number2):
    operators = '+-*'
    operator = choice(operators)
    if operator == '+':
        return number1 + number2, operator
    elif operator == '-':
        return number1 - number2, operator
    elif operator == '*':
        return number1 * number2, operator


def ask_question(number1, operator, number2):
    print(f'Question: {number1} {operator} {number2}')
    u_input = int(input('Your answer: '))
    return u_input


def generate_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer, operator = calculation(number1, number2)
    return answer, operator, number1, number2


def check_answer(u_input, answer):
    return u_input == answer


def main():
    count = 0
    name = welcome_user()
    while count < 3:
        print('What is the result of the expression?')
        answer, operator, number1, number2 = generate_question()
        u_input = ask_question(number1, operator, number2)
        if check_answer(u_input, answer):
            count += 1
            print('Correct!')
        else:
            print(f'{u_input} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
