# Jupyter web editor

#  ipython
import pandas

df1 = pandas.DataFrame([[2, 4, 6],[10, 20, 30]])

df1

# naming columns and indexes

df2 = pandas.DataFrame([[2, 4, 6],[10, 20, 30]],columns=["Price", "Age", "Value"])

df3 = pandas.DataFrame([[2, 4, 6],[10, 20, 30]],columns=["Price", "Age", "Value"], index=["First", "Second"])


# Passing Dictionaries

df4 = pandas.DataFrame([{"Name": "John"}, {"Name": "Jack"}])
df5 = pandas.DataFrame([{"Name": "John", "Surname": "Jones"}, {"Name": "Jack"}])

# read datastructure
# find average

type(df1) # pandas.core.frame.DataFrame

df1.mean()
df1.mean().mean()

type(df1.mean()) # pandas.core.series.Series

df3.Price
type(df3.Price) # pandas.core.series.Series

df3.Price.mean()
df3.Price.max()
df3.Price.min()


