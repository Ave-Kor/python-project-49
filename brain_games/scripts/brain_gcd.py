from brain_games.cli import welcome_user
from brain_games.games.game import ask_nod, generate_question_nod, calculation_nod, check_answer_nod


def main():
    count = 0
    name = welcome_user()
    while count < 3:
        print('Find the greatest common divisor of given numbers.')
        question_string, number1, number2, answer_nod = generate_question_nod()
        u_input = ask_nod(number1, number2)
        if check_answer_nod(u_input, answer_nod):
            count += 1
            print('Correct!')
        else:
            print(f'{u_input} is wrong answer ;(. Correct answer was {answer_nod}.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
