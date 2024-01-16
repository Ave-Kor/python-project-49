# импортируем функции
from brain_games.cli import welcome_user
from brain_games.games.game import ask_question, generate_question, check_answer


# начинаем игру
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
