import prompt
from brain_games.cli import welcome_user


def start_game(game):
    name = welcome_user()
    game.ask_question()
    count = 0
    while count < 3:
        question, answer = game.question_and_answer()
        print(f"Question: {question}")
        user_input = prompt.string("Your answer: ")
        if user_input.lower() != str(answer):
            print(f"'{user_input}' is wrong answer ;(.")
            print(f"Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    print(f"Congratulations, {name}!")
