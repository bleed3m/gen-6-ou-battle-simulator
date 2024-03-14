import pandas as pd
import pandasql as ps
'''
pokemon = pd.read_csv("pokemon.csv")
pokemon = pokemon.set_index("id")
# print(pokemon.query("type2 == 'Flying'"))

sql_query = "SELECT * FROM pokemon WHERE name == 'Gliscor'"
# print(ps.sqldf(sql_query, locals()))

# print(pokemon.head(5))

# Read Headers
# print(pokemon.columns)

# Read each column
print(pokemon[['name', 'type1']][0:2])
print(pokemon[['name']])

# Reach each row
print(pokemon.head(2))
print(pokemon.iloc[1]) # int location
for i, r in pokemon.iterrows():
    print(i, r)
print(pokemon.loc[pokemon['type1'] == "Ground"])
 
# Read a specific location (R, C)
print(pokemon.iloc[0, 0])
'''

import csv

with open('pokemon.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader)

    for line in csv_reader:
        print(line)