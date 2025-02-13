# Pipeline Data Quality

Para garantir a qualidade dos dados no processo de ETL vamos seguir os seguintes passos:

```mermaid
graph TD;
    A[Configura Variáveis do Banco] --> B[Ler Banco SQL];
    B --> E[Validação do Schema de Entrada];
    E -->|Falha| X[Alerta de Erro de Entrada];
    E -->|Sucesso| T[Transforma KPIs];
    T --> S[Validação Schema de Saída];
    S -->|Falha| Z[Alerta de Erro de Saída];
    S-->|Sucesso| F[Salvar no DuckDB]
```

## Contratos de Dados

### ::: app.schemas.ProdutoSchema

### ::: app.schemas.ProductSchemaKPI

## Funções de ETL

### ::: app.etl.extract_db

### ::: app.etl.transform

### ::: app.etl.load_to_duckdb
