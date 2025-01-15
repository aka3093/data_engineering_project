from scripts.data_processing import process_data
from scripts.dashboard_setup import run_dashboard
from scripts.data_quality import evaluate_data_quality

# Пути для хранения и загрузки данных
DATA_PATH = "./data/customer_segmentation_data.csv"
PROCESSED_PATH = "./output/processed_data.csv"
DATABASE_PATH = "./output/database.db"


def main():
    # Обработка данных из датасета
    process_data(DATA_PATH, PROCESSED_PATH, DATABASE_PATH)

    # Evaluate data quality
    evaluate_data_quality(PROCESSED_PATH)

    # Запуск дашборда на Streamlit
    run_dashboard(PROCESSED_PATH)


if __name__ == "__main__":
    main()
