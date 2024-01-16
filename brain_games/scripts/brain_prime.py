# импортируем функции
from brain_games.cli import welcome_user
from brain_games.games.game import (
    ask_prime,
    check_prime,
)


# начинаем игру
def main():
    count = 0
    name = welcome_user()
    while count < 3:
        user_input, number = ask_prime()
        if check_prime(user_input, number):
            count += 1
            print('Correct!')
        else:
            print(f'{user_input} is wrong answer ;(.')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
