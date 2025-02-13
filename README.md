## Pandera

### Validação com `strict`

Caso usarmos o valor `strict=True` em um schema do Pandera, só será aceito pela validação caso tenha exatamente o schema determinado. Caso contrário (tiver `strict=False`) colunas adicionais serão aceitas sem problemas.

Então para casos em que queremos ter certeza que os dados seguiram um formato expecífico usamos esse método, caso só quisermos assegurar que aquelas colunas determinadas que precisamos estão certas usamos o False.

### Validação em Modo `lazy`

Quando usamos o modo lazy todos os dados serão validados, sendo assim todos os dados serão lidos mesmo em caso de erro. O que não acontece no `lazy=False`, nesse caso no primeiro erro que ocorrer a aplicação já é parada e retorna esse erro exclusivo.

Sendo assim em conjuntos de dados grandes pode demorar mais, porém temos a visualização de todos os erros.
