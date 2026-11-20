
from src.extract import extract_data
from src.transform import transform_data
from src.data_quality import validate_data
from src.load import load_data

print("========== ETL PIPELINE STARTED ==========")

# Step 1: Extract
df = extract_data()

# Step 2: Transform
cleaned_df = transform_data(df)

# Step 3: Data Quality Validation
validated_df = validate_data(cleaned_df)

# Step 4: Load
load_data(validated_df)

print("\n========== ETL PIPELINE COMPLETED ==========")