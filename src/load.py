
from sqlalchemy import create_engine, URL, text, inspect
import os

def load_data(df):

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port=5432,
        database="ecommerce_db"
    )

    engine = create_engine(connection_url)

    try:

        # Check whether target table exists
        table_exists = inspect(engine).has_table("online_retail")

        if not table_exists:

            df.head(0).to_sql(
                name="online_retail",
                con=engine,
                if_exists="fail",
                index=False
            )

            print("Target table created!")

        # Create unique index
        with engine.begin() as connection:

            connection.execute(text("""
                CREATE UNIQUE INDEX IF NOT EXISTS
                idx_record_hash
                ON online_retail(record_hash)
            """))

        # Load data into staging table
        df.to_sql(
            name="retail_staging",
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=5000
        )

        # Insert only new records
        with engine.begin() as connection:

            connection.execute(text("""
                INSERT INTO online_retail
                SELECT *
                FROM retail_staging
                ON CONFLICT (record_hash) DO NOTHING
            """))

        print("Incremental loading completed successfully!")

        # Display final record count
        with engine.connect() as connection:

            count = connection.execute(
                text("SELECT COUNT(*) FROM online_retail")
            ).scalar()

            print("Total records in database:", count)

    except Exception as e:

        print("Error:", e)
        raise

    finally:

        engine.dispose()