import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_dashboard(file_path):
    st.title("Маркетинг. Дашборд по анализу данных заказчиков и компаний")

    # Загружаю данные
    data = pd.read_csv(file_path)
    with open('./output/encoding_mapping.json', 'r') as jsn:
        mapping = json.load(jsn)

    st.sidebar.subheader('Фильтр по возрасту')
    min_age = int(data['Age'].min())
    max_age = int(data['Age'].max())
    age_filter = st.sidebar.slider('Выбери диапазон возраста', min_value=min_age, max_value=max_age,
                                   value=(min_age, max_age))
    filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1])]

    # Отображаю базовую информацию по датасету
    st.subheader("Обзор датасета:")
    st.write(data.head())

    col1, col2 = st.columns(2)
    # Распределение возраста
    with col1:
        st.write("**Распределение возраста**")
        plt.figure(figsize=(5, 4))
        sns.histplot(filtered_data['Age'], kde=True, bins=20)
        plt.xticks(ticks=range(int(filtered_data['Age'].min()), int(filtered_data['Age'].max() + 1), 4))
        st.pyplot(plt)

    # Распределение уровня зарплаты
    with col2:
        st.write("**Распределение зарплаты**")
        plt.figure(figsize=(5, 4))
        sns.histplot(filtered_data['Income Level'], kde=True, bins=20)
        st.pyplot(plt)

    col3, col4 = st.columns(2)
    with col3:
        st.write('**Корреляция возраста и дохода**')
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=filtered_data, x='Gender', y='Income Level', hue='Gender')
        plt.legend(labels=['0 - Female', '1 - Male'])
        plt.title('Корреляция возраста и дохода')
        st.pyplot(plt)

    with col4:
        # Gender vs Communication Method
        st.write("**Корреляция пола и способа комуникации**")
        plt.figure(figsize=(6, 4))
        sns.countplot(data=filtered_data, x='Interactions with Customer Service', hue='Gender')
        plt.title("Корреляция пола и способа комуникации")
        plt.legend(title="Gender", labels=['0 - Female', '1 - Male'])
        labels = mapping['Interactions with Customer Service']
        plt.xticks(ticks=range(len(labels)), labels=labels)
        st.pyplot(plt)

    col5, col6 = st.columns(2)

    with col5:
        st.write('**Корреляция семейного статуса и дохода**')
        plt.figure(figsize=(6, 4))
        sns.countplot(data=filtered_data, x='Marital Status', hue='Gender')
        plt.title("Корреляция семейного статуса и дохода")
        plt.legend(title="Gender", labels=['0 - Female', '1 - Male'])
        labels = mapping['Marital Status']
        plt.xticks(ticks=range(len(labels)), labels=labels, ha='right', rotation=45)
        st.pyplot(plt)

    with col6:
        st.write('**Корреляция семейного статуса и дохода**')
        plt.figure(figsize=(6, 4))
        sns.countplot(data=filtered_data, x='Occupation', hue='Gender')
        plt.title("Корреляция семейного статуса и дохода")
        plt.legend(title="Gender", labels=['0 - Female', '1 - Male'])
        labels = mapping['Occupation']
        plt.xticks(ticks=range(len(labels)), labels=labels, ha='right', rotation=45)
        st.pyplot(plt)

    st.subheader("Выводы по проекту:")
    st.write(
        'Данный датасет был выбран для автоматизации обработки данных из датасета "Customer Segmentation Data".\n'
        'В ходе работы были выполнены следующие пункты:\n'
        '1. Первичный анализ датасета (выполнен в /scripts/dataset_review.py)\n'
        '2. После первичного анализа были выбраны столбцы, которые не потребуются для дальнейшей работы\n'
        '3. Данные были очищены от пустых значений (с заменой на средние значения)\n'
        '4. Удалены дубликаты из датасета'
        '   - 3-4 пункты добавлены в работу, но датасет был чистым изначально, поэтому удаление не потребовалось.\n'
        '5. После предобработки данных, были закодированы котегориальные колонки (например, Marital status, '
        'Education Level, Geographic Information) -> данный пункт нацелен для дальнейших анализов данных, либо'
        'обучения ML моделей и предсказания требуемых данных (для повышения конверсии, управления рекламой и т.д.)\n'
        '6. Построен дашборд с набором графиков для анализа данных по различным критериям (пол, возраст, уровень'
        'образования, взаимосвязь между разными показателями).\n'
        '7. Данный анализ датасета может быть полезен для дальнейшего изучения поведения покупателей, их потребностей,'
        'покупательской способности, анализу кастомеров, типам коммуникаций.\n\n'
        ''
        'Благодаря полученным данным можно оптимизировать и улучшить рекламные кампании.\n'
        'Провести оптимизацию ресурсов компаний (напрмиер, по типам коммуникации с клиентами).\n'
        'Выбрать новые продукты для ведения коммерческой деятельности, основываясь на целевой аудитории.\n'
    )

