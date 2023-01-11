"""Игра угадай число"""
import numpy as np
import random

def game_score(number:int=1) -> int:
    """Угадываем число
    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.
    Returns:
        int: с какой попытки угадали
    """
    random_number = random.randint(1, 101)
    count = 0
    start = 1
    finish = 100
    while True:
        count+=1
        predict_number = (start + finish) // 2
        if predict_number > number:
            finish = predict_number - 1
            predict_number = (finish + start) // 2
        elif predict_number < number:
            start = predict_number + 1
            predict_number = (finish + start) // 2
        else:
            print(f'Алгоритм рассчитал число {number} за {count} попыток')
            break 
    return count

def count_attempts(game_score) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        game_score ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    attempts = []
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        attempts.append(game_score(number))
    score = int(np.mean(attempts)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
# RUN
if __name__ == '__main__':
    count_attempts(game_score)