import pandas as pd

# Load the dataset to analyze its structure and content
file_path = '../data/customer_segmentation_data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
'''Вывожу общую информация по датасету:'''
print('\nПервые строки:')
print(data.head(n=5))
print('\nИнфо по датасету:')
print(data.info())

'''Проверка датасета на пустые значения'''
print('\nПроверка на пустые значения:')
print(data.isnull().sum())

'''Проверка датасета на дублирующиеся строки'''
print('\nПроверка на дублирующиеся строки:')
print(data.duplicated().sum())

'''Просмотр описания датасета для дальнейшей работы'''
print('\nОбщая информация по датасету:')
print(data.describe(include='all'))

'''
Результаты проверки датасета:
1. Пропущенные значения отсутствуют во всех колонках, что упрощает обработку данных.
2. Дублирующихся строк также не найдено в датасете.
3. В датасете присутствуют колонки как с числовыми данными ("Age", "Income Level", "Coverage Amount", "Premium Amount"),
так и категориальными данными (например, "Gender", "Marital Status", "Education Level" и др.).
Категориальные данные имеют небольшое количество уникальных значений.
4. Из датасета будут удалены следующие колонки, так как не требуются для анализа:
Behavioral Data, Insurance Products Owned, Coverage Amount, Premium Amount, Policy Type, Segmentation Group
'''