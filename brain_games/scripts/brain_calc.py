from random import randint
from random import choice
from brain_games.cli import welcome_user


def main():
    count = 0
    name = welcome_user()

    while count < 3:
        print('What is the result of the expression?')
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operators = '+-*'
        operator = choice(operators)

        def calculation(number1, number2, operator):
            if operator == '+':
                return number1 + number2
            elif operator == '-':
                return number1 - number2
            elif operator == '*':
                return number1 * number2
        print(f'Question: {number1} {operator} {number2}')
        answer = calculation(number1, number2, operator)
        user_input = int(input('Your answer: '))
        if user_input == answer:
            count += 1
            print('Correct!')
        else:
            print(f'{user_input} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
