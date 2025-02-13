# Pandera

Pandera é uma ferramenta usada para validação de estrutura em formato DataFrame, sendo recomendado para Pandas, Polars, DuckDB, PySpark e etc. Sendo que essa ferramenta ainda pode ser usada para inferência de Schema, o que ajuda a criar um processo de qualidade em Pipelines já existentes.

Diferente do Pydantic que é recomendado para estruturas mais simples, como objetos, tipos primitivos, API's e Dataframes menores (até 1M de linhas), o Pandera vai ajudar com validações maiores.

Sendo que o Pandera ainda trás validações úteis para regras mais complexas, como validações de hipótese.

Importante notar que essa ferramenta pode gerar impacto na velocidade da Pipeline, porém trazendo uma maior segurança quanto a qualidade dos dados na pipeline!

## Validação com `strict`

Caso usarmos o valor `strict=True` em um schema do Pandera, só será aceito pela validação caso tenha exatamente o schema determinado. Caso contrário (tiver `strict=False`) colunas adicionais serão aceitas sem problemas.

Então para casos em que queremos ter certeza que os dados seguiram um formato expecífico usamos esse método, caso só quisermos assegurar que aquelas colunas determinadas que precisamos estão certas usamos o False.

## Validação em Modo `lazy`

Quando usamos o modo lazy todos os dados serão validados, sendo assim todos os dados serão lidos mesmo em caso de erro. O que não acontece no `lazy=False`, nesse caso no primeiro erro que ocorrer a aplicação já é parada e retorna esse erro exclusivo.

Sendo assim em conjuntos de dados grandes pode demorar mais, porém temos a visualização de todos os erros.
