import pandas as pd

def evaluate_data_quality(file_path):
    """Evaluate the quality of the dataset and print a report."""
    data = pd.read_csv(file_path)

    print("Data Quality Report:")

    # Check for missing values
    missing_values = data.isnull().sum()
    print("\nMissing Values:")
    print(missing_values[missing_values > 0])

    # Check for duplicates
    duplicate_count = data.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicate_count}")

    # Check for outliers in numeric columns
    print("\nOutliers per numeric column:")
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        print(f"{col}: {len(outliers)} outliers")

    # Check distribution of categorical columns
    print("\nCategorical Columns Distribution:")
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        print(f"\n{col} distribution:")
        print(data[col].value_counts())