import pandas as pd  # Импортируем библиотеку pandas для работы с DataFrame
import random  # Импортируем библиотеку random для перемешивания списка

lst = ['robot'] * 10  # Создаем список из 10 элементов 'robot'
lst += ['human'] * 10  # Добавляем к списку 10 элементов 'human'
random.shuffle(lst)  # Перемешиваем список lst

data = pd.DataFrame({'whoAmI': lst})  # Создаем DataFrame из списка lst с одним столбцом 'whoAmI'
print("Исходный DataFrame:")  # Печатаем текст "Исходный DataFrame:"
print(data.head())  # Выводим первые 5 строк DataFrame data

unique_values = data['whoAmI'].unique()  # Получаем уникальные значения из столбца 'whoAmI'
one_hot_data = pd.DataFrame()  # Создаем пустой DataFrame для one hot encoding

for value in unique_values:  # Проходим по каждому уникальному значению
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)  # Создаем столбец для каждого уникального значения,
                                                                 # где 1 означает соответствие текущему значению, а 0 - несоответствие

print("\nOne Hot DataFrame:")  # Печатаем текст "One Hot DataFrame:"
print(one_hot_data.head())  # Выводим первые 5 строк DataFrame one_hot_data

