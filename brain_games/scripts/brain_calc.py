from random import randint
from random import choice
from brain_games.cli import welcome_user


def main():
    count = 0
    name = welcome_user()

    while count < 3:
        random_number = randint(1, 100)
        print('What is the result of the expression?')
        number1 = random_number
        number2 = random_number
        operators = '+-*'
        operator = choice(operators)

        def random_operator(number1, number2, operator):
            if operator == '+':
                return number1 + number2
            elif operator == '-':
                return number1 - number2
            elif operator == '*':
                return number1 * number2
        print(f'Question: {number1} {operator} {number2}')
        rigth_answer = random_operator(number1, number2, operator)
        user_input = int(input('Your answer: '))
        if user_input == rigth_answer:
            count += 1
            print('Correct!')
        else:
            print(f'{user_input} is wrong answer ;(. Correct answer was {rigth_answer}.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
