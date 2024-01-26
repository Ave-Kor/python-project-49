import random


GAME_QUEST = 'What number is missing in the progression?'


# генерируем вопрос и ответ для progression
def question_and_answer():
    number = random.randint(1, 100)
    question_string = [number]
    step = random.randint(1, 100)
    current_number = number
    while len(question_string) < 10:
        current_number += step
        question_string.append(current_number)
    random_index = random.randint(0, len(question_string) - 1)
    answer = question_string[random_index]
    question_string[random_index] = ".."
    question = ' '.join(str(num) for num in question_string)
    return question, answer
