import random
from brain_games.constants import (
    MIN_RANDOM_NUMBER,
    MAX_RANDOM_NUMBER,
    MAX_PROGRESSION_LENGTH)


GAME_QUEST = 'What number is missing in the progression?'


# генерируем вопрос и ответ для progression
def question_and_answer():
    """Brain-progression

    Цель игры: определить число, которое замененно в арифметической прогресси
    двумя точками.

    """
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    difference = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    sequence = make_progression(number, difference)
    random_index = random.randint(0, len(sequence) - 1)
    answer = sequence[random_index]
    sequence[random_index] = ".."
    question = ' '.join(str(num) for num in sequence)
    return question, answer


# создаем прогрессию
def make_progression(number, difference):
    progression = [number]
    current_number = progression[0]
    sequence = list(progression)
    while len(sequence) < MAX_PROGRESSION_LENGTH:
        current_number += difference
        sequence.append(current_number)
    return sequence
