from randobrain-even import randint
from brain_games.cli import welcome_user


def main():
    count = 0
    name = welcome_user()

    while count <= 3:
        random_number = randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question: ', random_number)
        user_input = input('Your answer: ')
        if user_input == 'yes' and random_number % 2 == 0:
            count += 1
            return 'Correct!'
        elif user_input == 'yes' and random_number % 2 != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again," + name + "!")
            break
        elif user_input == 'no' and random_number % 2 != 0:
            count += 1
            return 'Correct!'
        elif user_input == 'no' and random_number % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again," + name + "!")
            break
        else:
            print("Answer is wrong ;(. Type only 'yes' or 'no'.")
            print("Let's try again," + name + "!")
            break
    print("Congratulations," + name + "!")


if __name__ == '__main__':
    main()
