import os
print(os.listdir())

import pandas
df1 = pandas.read_csv("supermarkets.csv")
print(df1)

df1.set_index("ID")
df1.shape

df2 = pandas.read_json("supermarkets.json")
df2.set_index("ID")

df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
df3.set_index("ID")

df4 = pandas.read_csv("supermarkets_commas.txt")
df4.set_index("ID")

df5 = pandas.read_csv("supermarkets_semi-colons.txt", sep=";")
df5.set_index("ID")

# https://pythonhow.com/supermarkets.json
# https://pythonhow.com/supermarkets.csv

df6 = pandas.read_json("https://pythonhow.com/supermarkets.json")
df6.set_index("ID")