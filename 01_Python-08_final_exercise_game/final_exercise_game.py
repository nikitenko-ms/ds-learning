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

    while True: # создаем цикл для угадывания
        count += 1 # каждая попытка увеличивает счетчик на 1
        
        if number < 35: # с помощью условий тут и далее в цикле создаем "воронку" для сокращения количества попыток
            if number < 18:
                predict_number = np.random.randint(1, 18) # компьютер предлагает число 
                if predict_number == number: # если число верное, то происходит выход из цикла
                    break
            else:
                predict_number = np.random.randint(18, 35)
                if predict_number == number:
                    break
        
        elif 35 <= number < 70:
            if number < 53:
                predict_number = np.random.randint(35, 53) 
                if predict_number == number:
                    break
            else:
                predict_number = np.random.randint(53, 70) 
                if predict_number == number:
                    break
        
        else:
            if 70 <= number < 85:
                predict_number = np.random.randint(70, 85) 
                if predict_number == number:
                    break
            else:
                predict_number = np.random.randint(85, 101) 
                if predict_number == number:
                    break
    
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