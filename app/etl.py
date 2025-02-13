import duckdb
import pandas as pd
import pandera as pa
from database import get_engine
from schemas import ProductSchemaKPI, ProdutoSchema


@pa.check_output(ProdutoSchema, lazy=True)
def extract_db(query: str) -> pd.DataFrame:
    """
    Extrai dados do banco de dados SQL usando a consulta fornecida.

    Args:
        query: A consulta SQL para extrair dados.

    Returns:
        Um DataFrame do Pandas contendo os dados extraídos.
    """
    engine = get_engine()
    with engine.connect() as conn, conn.begin():
        return pd.read_sql_query(query, conn)


@pa.check_input(ProdutoSchema, lazy=True)
@pa.check_output(ProductSchemaKPI, lazy=True)
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma os dados do DataFrame aplicando cálculos e normalizações.

    Args:
        df: DataFrame do Pandas contendo os dados originais.

    Returns:
        DataFrame do Pandas após a aplicação das transformações.
    """
    df["valor_total_estoque"] = df["quantidade"] * df["preco"]
    df["categoria_normalizada"] = df["categoria"].str.lower()
    df["disponibilidade"] = df["quantidade"] > 0

    return df


@pa.check_input(ProductSchemaKPI, lazy=True)
def load_to_duckdb(df: pd.DataFrame, table_name: str, db_file: str = "my_duckdb.db"):
    """
    Carrega o DataFrame no DuckDB, criando ou substituindo a tabela especificada.

    Args:
        df: DataFrame do Pandas para ser carregado no DuckDB.
        table_name: Nome da tabela no DuckDB onde os dados serão inseridos.
        db_file: Caminho para o arquivo DuckDB. Se não existir, será criado.
    """
    with duckdb.connect(database=db_file, read_only=False) as con:
        con.register("df_temp", df)
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df_temp")


if __name__ == "__main__":
    q = "SELECT * FROM produtos_bronze_email"
    df_products = extract_db(q)
    df_products_kpi = transform(df_products)
    # pa.infer_schema(df_products).to_script("./app/product_schema.py")

    load_to_duckdb(df_products_kpi, table_name="products_kpi")
