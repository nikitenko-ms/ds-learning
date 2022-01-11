""" Игра: "Угадай число """

import numpy as np

# загадываем число
number = np.random.randint(1, 101) 

# считаем количество попыток
count = 0

# создаем цикл для угадывания
while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
                        
    if predict_number > number:
        print('Загаданное чило меньше введенного')  
    elif predict_number < number:
        print('Загаданное чило больше введенного')          
    else:
        print(f'Вы угадали число за {count} попыток! Загаданно число - {number}')
        break