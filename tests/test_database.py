from app.database import load_settings, get_engine, query_from_database
from pandas import DataFrame
from sqlalchemy import Engine

def test_load_settings():
    settings = load_settings()
    settings_keys = ["db_host", "db_port", "db_user", "db_password", "db_name"]

    assert isinstance(settings, dict)
    assert list(settings.keys()) == settings_keys
    assert all([isinstance(v, str) for v in settings.values()])

def test_get_engine():
    engine = get_engine()
    
    assert isinstance(engine, Engine)

def test_query_from_database():
    q = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
    df = query_from_database(q)
    
    assert isinstance(df, DataFrame)
    assert df['table_name'].count() > 0