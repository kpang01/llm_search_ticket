import pandas as pd
from sqlalchemy import create_engine

# Read the CSV
df = pd.read_csv('../customer_support_tickets.csv')

engine = create_engine("postgresql://llm_ticket_user:H9GUJMumL4nVkDcA6crejdo5niMzWOI8@dpg-d3vo04ripnbc739qifm0-a.singapore-postgres.render.com/llm_ticket")

# Insert data into the database
df.to_sql('customer_support_ticket', engine, if_exists='replace', index=False)

print("Data inserted successfully.")
