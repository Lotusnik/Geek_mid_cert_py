import pandas as pd  # Импортируем библиотеку pandas для работы с DataFrame
import random  # Импортируем библиотеку random для перемешивания списка

lst = ['robot'] * 10  # Создаем список из 10 элементов 'robot'
lst += ['human'] * 10  # Добавляем к списку 10 элементов 'human'
random.shuffle(lst)  # Перемешиваем список lst

data = pd.DataFrame({'whoAmI': lst})  # Создаем DataFrame из списка lst с одним столбцом 'whoAmI'
print("Исходный DataFrame:")  # Печатаем текст "Исходный DataFrame:"
print(data.head())  # Выводим первые 5 строк DataFrame data

one_hot_data = data['whoAmI'].apply(lambda x: pd.Series({v: int(v == x) for v in data['whoAmI'].unique()}))
# Применяем функцию к каждому элементу столбца 'whoAmI' для создания one hot encoding
# Функция создает Series, где ключи - уникальные значения из столбца 'whoAmI',
# а значения - 1 или 0 в зависимости от соответствия текущему элементу

print("\nOne Hot DataFrame:")  # Печатаем текст "One Hot DataFrame:"
print(one_hot_data.head())  # Выводим первые 5 строк DataFrame one_hot_data
