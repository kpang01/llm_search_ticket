import pandas as pd
from db.de_connection import get_db_engine
from db.ticket_field import TICKET_METADATA_FIELDS

def generate_select_sql(table_name : str, columns: list = None) -> str:
    """
    Generate a SELECT SQL query.
    
    Args:
        table_name (str): Name of the table to query.
        columns (list or None): List of columns to select. If None, selects all columns.
    
    Returns:
        str: The generated SQL query.
    """
    if columns is None:
        columns = TICKET_METADATA_FIELDS
    column_str = ', '.join([f'"{col}"' for col in columns])
    sql_query = f'SELECT {column_str} FROM {table_name}'
    return sql_query

def fetch_data_as_dataframe(query, params=None) -> list:
    """Fetch data from the database and return it as a pandas DataFrame."""
    engine = get_db_engine()
    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection, params=params)
    return df

def separate_metadata_and_description(dataset, desc_key='Ticket Description') -> list:
    """
    Separate metadata and description from the DataFrame.
    
    Args:
        dataset: List of dictionaries representing the dataset.
        desc_key (str): Key for the description field.

    Returns:
        tuple: (list of description dicts, list of metadata dicts)
    """
    metadata_list = []
    desc_list = []
    dataset = pd.DataFrame(dataset)  # Ensure dataset is a DataFrame for uniform processing
    if isinstance(dataset, pd.DataFrame):
        for _, row in dataset.iterrows():
            
            desc_list.append({row.get(desc_key)})
            meta = {k: v for k, v in row.items() if k != desc_key}
            metadata_list.append(meta)
    else:
        raise ValueError("Dataset must be a list of dicts or pandas DataFrame.")

    return desc_list, metadata_list