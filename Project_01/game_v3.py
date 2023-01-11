"""Игра угадай число"""
import numpy as np
import random

def random_predict(number:int=1) -> int:
    """Угадываем число
    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.
    Returns:
        int: с какой попытки угадали
    """
    random_number = random.randint(1, 101)
    count = 0 # задаем счетчик
    min_num = 1 # вводим переменную для минимального значения
    max_num = 100 # вводим переменную для максимального значения
    
    while True:
        count+=1
        predict_number = (min_num + max_num) // 2
        if predict_number > number:
            max_num = predict_number - 1
            predict_number = (max_num + min_num) // 2
        elif predict_number < number:
            min_num = predict_number + 1
            predict_number = (max_num + min_num) // 2
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
    count_attempts(random_predict)