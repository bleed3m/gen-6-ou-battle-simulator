import pandas as pd
import pandasql as ps

data = pd.read_csv("pokemon.csv")
data = data.set_index("id")
print(data.query("type2 == 'Flying'"))