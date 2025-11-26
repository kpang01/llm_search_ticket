import pandas as pd
from sqlalchemy import create_engine

# Connection string format: postgresql://username:password@host:port/database
engine = create_engine('postgresql://llm_ticket_user:H9GUJMumL4nVkDcA6crejdo5niMzWOI8@dpg-d3vo04ripnbc739qifm0-a.singapore-postgres.render.com/llm_ticket')

# Read data into pandas DataFrame
df = pd.read_sql('SELECT * FROM customer_support_ticket', engine)

print(df)

