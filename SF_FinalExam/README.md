# Онлайн-школа SkillFactory
# Финальный экзамен. "Predict Student Performance from Game Play"

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)  
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[5. Результат](README.md#Результат)    
[6. Выводы](README.md#Выводы) 

### Описание проекта    
Необходимо выбрать и реализовать прокт, который позволит продемонстрировать основные навыки, полученные во время обучения в онлайн-школе SkillFactory на специальности Data Science.

[к оглавлению](README.md#Оглавление)


### Какой кейс решаем?    
Обучение должно быть увлекательным, и здесь на помощь приходит обучение, основанное на играх. Такой образовательный подход позволяет учащимся взаимодействовать с образовательным контентом в игровой форме, делая его приятным и динамичным. Несмотря на то, что обучение на основе игр используется во все большем числе образовательных учреждений, по-прежнему существует ограниченное количество открытых наборов данных, доступных для применения принципов data science для улучшения обучения на основе игр.
Большинство обучающих платформ, основанных на играх, недостаточно используют отслеживание знаний для поддержки отдельных учащихся. Методы отслеживания знаний были разработаны и изучены в контексте онлайн-сред обучения и интеллектуальных систем репетиторства. Но в обучающих играх отслеживанию знаний уделяется меньше внимания.

В случае достижения успехов в проекте, разработчики получат возможность улучшать обучающие игры и оказывать дальнейшую поддержку преподавателям, с помощью информационных панелей и аналитических инструментов.


**Условия:**  
В соревновании необходимо спрогнозировать успеваемость учащихся во время обучения на основе игр в режиме реального времени. 
Данная работа призвана помочь продвинуть исследования в области методов отслеживания знаний для обучения, основанного на играх. Проект направлен на поддержку разработчиков развивающих игр, чтобы создать более эффективный опыт обучения для студентов.


**Метрика оценки результата**     
Основной метрикой, по которой оценивается эффективность модели в соревновании является метрика F1, которая показывает некий сбалансированный результат метрик recall и precision, т.е. дает общее представление о точности и полноте. Однако данная метрика не имеет бизнес-интерпритации. Для соревнования, чем больше – тем лучше.


### Краткая информация о данных
В качестве данных используются датасет содержащий записи о действиях игроков. Датасет содержит данные для 11779 сеансов. Состав и расшифровка всех признаков представлена в рабочем ноутбуке.
Исходные данные можно получить на платформе Kaggle, в соотвтетствующем соревновании (https://www.kaggle.com/competitions/predict-student-performance-from-game-play).
  
[к оглавлению](README.md#Оглавление)


### Этапы работы над проектом  
Проект состоит из следующих этапов:
1. Загрузка данных и инструментов для их обработки;
2. Исследование данных;
3. Формирование новых признаков;
4. Очистка от выбросов;
5. Отбор признаков;
6. Нормализация/стандартизация, оценка корреляции;
7. Построение модели;
8. Подбор гиперпараметров;
9. Вывод.

[к оглавлению](README.md#Оглавление)


### Результат
В результате работы над данными, удалось преобразовать признаки и построить модель. Лучший показатель метрики f1 - 0.85

[к оглавлению](README.md#Оглавление)


### Выводы
Выводы представлены по ходу выполнения проекта в рабочем ноутбуке.

[к оглавлению](README.md#Оглавление)