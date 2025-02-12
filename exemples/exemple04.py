import pandas as pd
import pandera as pa

df = pd.DataFrame({
    "column1": [5, 10, 20],
    "column2": ["a", "b", "c"],
    "column3": pd.to_datetime(["2010", "2011", "2012"]),
})
schema = pa.infer_schema(df)
# can infer a schema, need to be validated, but create a schema auto based on Df data

with open("./exemples/inferred_schema.py", "w") as file:
         file.write(schema.to_script())