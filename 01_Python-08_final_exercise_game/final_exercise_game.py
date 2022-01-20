""" Компьютер сам загадывает и сам угадывает произвольное число в диапазоне 1-101
    Происходит подсчет среднего количества попыток угадывания на основе 1000 проходов
"""

import numpy as np # импортируем библиотеку NumPy


def random_predict(number:int=1) -> int:
    """Функция угадывания числа
    
    Args:
        number (int): загаданное число. По умолчанию 1.
    Returns:
        int: число попыток
    """
    count = 0 # задаем счетчик количества попыток
    min_number = 1 # задаем нижнюю возможную границу поиска
    max_number = 100 # задаем верхнюю возможную границу поиска
    
    while min_number < max_number: # создаем цикл для угадывания
        count += 1 # каждая попытка увеличивает счетчик на 1
        predict_number = np.random.randint(min_number, max_number + 1)  # предполагаемое число внутри заданных границ
        middle_number = (min_number + max_number) // 2 # задаем середину диапазон
        
        if predict_number == number:   # если угадали число, 
            break                      # то выходим из цикла
        elif number > middle_number:   # если загаданное число в диапазоне выше середины,
            min_number = middle_number # то сдвигаем нижнюю границу к середине        
        else:                          # если загаданное числло в диапазоне ниже середины.
            max_number = middle_number # то сдвигаем верхнюю границу к середине 
    
    return count # функция возвращает количество попыток


def score_game(random_predict) -> int:
    """Функция подсчета среднего количества попыток угадывания за 1000 проходов
    
    Args:
        random_predict: функция угадывания числа
    Returns:
        int: среднее количества попыток
    """
    count_list = [] # задаем пустой список для добавления случайных чисел
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # задаем генератор случаных числе размером в 1000 чисел
    
    for number in random_array:
        count_list.append(random_predict(number)) # цикл добавляет в список количество попыток угадывания числа
        
    score = int(np.mean(count_list)) # в перменную записывает среднее число попыток
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    
    return score

score_game(random_predict) # вызов функции score_game, в качестве аргумента - функция random_predict