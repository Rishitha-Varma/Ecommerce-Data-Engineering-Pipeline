def validate_data(df):

    print("\n========== DATA QUALITY CHECKS ==========")

    # 1. Check total records
    print("Total Records:", len(df))

    # 2. Check duplicate records
    duplicates = df.duplicated().sum()

    print("Duplicate Records:", duplicates)

    # 3. Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # 4. Check invalid quantities
    invalid_quantity = (df['Quantity'] <= 0).sum()

    print("\nInvalid Quantities:", invalid_quantity)

    # 5. Check invalid prices
    invalid_prices = (df['UnitPrice'] <= 0).sum()

    print("Invalid Prices:", invalid_prices)

    # 6. Check missing transaction IDs
    missing_invoice = df['InvoiceNo'].isnull().sum()

    print("Missing Invoice Numbers:", missing_invoice)

    # 7. Check negative transaction amounts
    invalid_amount = (df['TotalAmount'] <= 0).sum()

    print("Invalid Transaction Amounts:", invalid_amount)

    # Final validation
    if duplicates == 0 and invalid_quantity == 0 and invalid_prices == 0:
        print("\nDATA QUALITY STATUS: PASSED")
    else:
        print("\nDATA QUALITY STATUS: FAILED")

    print("=========================================")

    return df