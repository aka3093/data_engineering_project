import sqlite3
import pandas as pd
import json

def process_data(input_path, output_path, db_path):
    # Загружаю данные
    try:
        data = pd.read_csv(input_path)
    except FileNotFoundError:
        raise ImportError('File has not been found, Please specify the correct path')

    # Удаляю ненужные колонки
    columns_to_drop = ['Behavioral Data', 'Insurance Products Owned', 'Coverage Amount', 'Premium Amount',
                       'Policy Type', 'Segmentation Group']
    data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Дропаем дубли и обрабатываем пустые значения
    # Пустые значения меняем на среднее
    data.drop_duplicates(inplace=True)
    data.fillna(data.mean(numeric_only=True), inplace=True)

    # Удаляю выбросы
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

    # Кодируем категориальные значения
    categorical_columns = ['Gender', 'Marital Status', 'Education Level', 'Geographic Information', 'Occupation',
                           'Interactions with Customer Service', 'Customer Preferences']
    encoding_mapping = {}
    for col in categorical_columns:
        if col in data.columns:
            unique_values = data[col].unique()
            mapping = {val: idx for idx, val in enumerate(unique_values)}
            encoding_mapping[col] = mapping
            data[col] = data[col].map(mapping)

    # Сохраняю закодированные значения для информации
    encoding_path = './output/encoding_mapping.json'
    with open(encoding_path, 'w') as f:
        json.dump(encoding_mapping, f, indent=4)

    # Сохраняю обработанный датасет
    data.to_csv(output_path, index=False)

    # Переношу данные в БД
    with sqlite3.connect(db_path) as conn:
        data.to_sql('customers', conn, if_exists='replace', index=False, chunksize=500)
        print(f"The data has been successfully saved to DB {db_path} in the table customers.")

