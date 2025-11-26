import psycopg2
from db.db_config import DATABASE_CONFIG
from sqlalchemy import create_engine

def execute_query(query, params=None):
    params = params or ()
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_db_engine():
    """Create and return a SQLAlchemy engine using the database configuration."""
    db_url = (f"postgresql+psycopg2://{DATABASE_CONFIG['user']}:"
              f"{DATABASE_CONFIG['password']}@"
              f"{DATABASE_CONFIG['host']}:"
              f"{DATABASE_CONFIG['port']}/"
              f"{DATABASE_CONFIG['database']}")
    engine = create_engine(db_url)
    return engine