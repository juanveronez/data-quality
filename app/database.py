from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

def load_settings():
    """
    Load database settings from .env file
    
    return: {"db_host": str, "db_port": str, "db_user": str, "db_password": str, "db_name": str}
    """
    load_dotenv()

    settings = {
        'db_host': os.getenv('POSTGRES_HOST'),
        'db_port': os.getenv('POSTGRES_PORT'),
        'db_user': os.getenv('POSTGRES_USER'),
        'db_password': os.getenv('POSTGRES_PASSWORD'),
        'db_name': os.getenv('POSTGRES_DB')
    }

    return settings

def get_engine():
    """
    Get a database engine using SQL Alchemy
    """
    s = load_settings()
    connection_url = f"postgresql://{s["db_user"]}:{s["db_password"]}@{s["db_host"]}:{s["db_port"]}/{s["db_name"]}"

    engine = create_engine(url=connection_url)
    return engine
    

def query_from_database(query: str) -> pd.DataFrame:
    """
    Execute SQL Query and return Pandas Dataframe
    """
    engine = get_engine()
    with engine.connect() as conn, conn.begin():
        return pd.read_sql_query(query, conn)
