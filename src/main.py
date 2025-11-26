# from fastapi import FastAPI
# from src.api.endpoints import router

# app = FastAPI()
# app.include_router(router)
import pandas as pd
from db.de_connection import execute_query


def main():
    try: 
        query = "SELECT * FROM customer_support_ticket"
        rows = execute_query(query)
        print("Database connection successful. Retrieved rows:")
        print(f"Total rows: {len(rows)}")
        df = pd.DataFrame(rows)
        print("Database connected successfully.")
        print(f"Total rows fetched: {len(df)}")
        print(df)
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    main()

    