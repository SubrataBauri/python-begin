df7 = pandas.read_json("https://pythonhow.com/supermarkets.json")
df7 = df7.set_index("Address")

df7.loc["735 Dolores St":"1056 Sanchez St", "Country":"Name"]

# one cell
df7.loc[:"1056 Sanchez St", "Country":"Name"]

df7.loc[:, "Country":"Name"]

# convert to list
list(df7.loc[:, "Country"])

# index based slicing
df7.iloc[1:4,1:4]

# deprecated
df7.ix[3,"Name"]