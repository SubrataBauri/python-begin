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

# deleting rows and columns
df7 = df7.drop(2,0) # 0 for rows
df7.drop("City",1) # 1 for columns


df7.drop("332 Hill St",0) # threw error
"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-46-fb74d999cc85> in <module>()
----> 1 df7.drop("332 Hill St",0)

c:\users\subrata\pycharmprojects\python-mega\venv\lib\site-packages\pandas\core\generic.py in drop(self, labels, axis, index, columns, level, inplace, errors)
   2528         for axis, labels in axes.items():
   2529             if labels is not None:
-> 2530                 obj = obj._drop_axis(labels, axis, level=level, errors=errors)
   2531 
   2532         if inplace:

c:\users\subrata\pycharmprojects\python-mega\venv\lib\site-packages\pandas\core\generic.py in _drop_axis(self, labels, axis, level, errors)
   2560                 new_axis = axis.drop(labels, level=level, errors=errors)
   2561             else:
-> 2562                 new_axis = axis.drop(labels, errors=errors)
   2563             dropped = self.reindex(**{axis_name: new_axis})
   2564             try:

c:\users\subrata\pycharmprojects\python-mega\venv\lib\site-packages\pandas\core\indexes\base.py in drop(self, labels, errors)
   3742             if errors != 'ignore':
   3743                 raise ValueError('labels %s not contained in axis' %
-> 3744                                  labels[mask])
   3745             indexer = indexer[~mask]
   3746         return self.delete(indexer)

ValueError: labels ['332 Hill St'] not contained in axis
"""


# Adding data to dataframe

len(df7.index)
df7["Continent"] = df7.shape[0]*["North America"]
df7

# modify column
df7["Continent"] = df7["Country"] + "," + "North America"

# add row
df7_t = df7.T # Transpose - change rows to columns and vice versa
df7_t

df7_t["My address"] = ["new address", "My city","My country", 10, 2, "my name", "My state", "My continent"]
df7_t

df7 = df7_t.T
df7