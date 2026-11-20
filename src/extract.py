import pandas as pd
def extract_data():
    file_path = "data/raw/Online Retail.xlsx"
    df = pd.read_excel(file_path)
    print("Data extracted successfully!")
    print("\nFirst 5 records:")
    print(df.head())
    print("\nDataset shape:")
    print(df.shape)
    print("\nColumn Info:")
    print(df.info())
    return df