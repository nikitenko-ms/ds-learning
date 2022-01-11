""" Компьютер сам угадывает число, переданное в функцию
    Происходит подсчет среднего количества попыток для угадывания
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Функция угадывания числа
    
    Args:
        number (int): Загаданное число. По умолчанию 1.
    Returns:
        int: Число попыток
    """
    count = 0 # считаем количество попыток

    while True: # создаем цикл для угадывания
       count += 1 # подсчет попыток
       predict_number = np.random.randint(1, 101) # компьютер предлагает число
       if predict_number == number:
           break # выход из цикла при попадании в нужное число
    return count

#print(f'Компьютер угадал число за {random_predict(24)} попыток')


def score_game(random_predict) -> int:
    """Функция подсчета среднего количества попыток угадывания за 1000 проходов
    
    Args:
        random_predict: функция угадывания числа
    Returns:
        int: среднее количества попыток
    """
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return score

if __name__ == '__main__':
    score_game(random_predict)