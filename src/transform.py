import pandas as pd
from pandas.util import hash_pandas_object
def transform_data(df):
    print("\nStarting data transformation...")

    df = df.copy()
    df = df.drop_duplicates()
    print("Duplicates removed.")
    df = df.dropna(subset=['Description'])
    print("Missing product descriptions removed.")
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    print("Cancelled transactions removed.")
    df = df[df['Quantity']>0]
    df=df[df['UnitPrice']>0]
    print("Invalid transactions removed.")
    df['CustomerID'] = df['CustomerID'].astype('Int64')
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceMonth'] = df['InvoiceDate'].dt.month
    df['InvoiceYear'] = df['InvoiceDate'].dt.year
    print("\nTransformation completed successfully!")
    print("\nCleaned Dataset Shape:")
    print(df.shape)
    # Generate a unique hash for each transaction record
    hash_columns = [
        'InvoiceNo',
        'StockCode',
        'Description',
        'Quantity',
        'InvoiceDate',
        'UnitPrice',
        'CustomerID',
        'Country'
    ]

    df['record_hash'] = hash_pandas_object(
        df[hash_columns].astype('string'),
        index=False
    ).astype('uint64').astype(str)
    return df