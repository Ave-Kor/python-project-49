# импортитуем функции
from brain_games.cli import welcome_user
from brain_games.games.game import (
    generate_number,
    ask_even,
    ask_input,
    check_even,
)


def main():
    count = 0
    name = welcome_user()

    # вводим счётчик раундов
    while count < 3:
        random_number = generate_number()
        ask_even(random_number)
        user_input = ask_input()
        if check_even(user_input, random_number, name):
            count += 1
        else:
            break
    if count == 3:
        print(f'''Congratulations, {name}!''')


if __name__ == '__main__':
    main()
