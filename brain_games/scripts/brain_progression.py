from brain_games.cli import welcome_user
from brain_games.games.game import (
    generate_question_prog,
    ask_prog,
    ask_input,
    check_prog,
)


def main():
    count = 0
    name = welcome_user()
    while count < 3:
        question_string, answer = generate_question_prog()
        ask_prog(question_string)
        user_input = str(ask_input())
        if check_prog(user_input, answer):
            count += 1
            print('Correct!')
        else:
            print(f'{user_input} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'''Congratulations, {name}!''')


if __name__ == '__main__':
    main()
