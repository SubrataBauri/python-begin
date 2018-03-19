# pip install geopy
import geopy
dir(geopy)

from geopy.geocoders import Nominatim
nom =  Nominatim()
nom.geocode("3995 23rd St, San Francisco, CA 94114")

n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
n.latitude
n.longitude

import pandas
df8 = pandas.read_csv("supermarkets.csv")
df8["Address"] = df8["Address"] + ", " + df8["City"] +  ", " + df8["State"] +  ", " + df8["Country"]
df8

df8["Coordinate"] = df8["Address"].apply(nom.geocode)
df8.Coordinate

df8["latitude"] = df8["Coordinate"].apply(lambda x: x.latitude if x != None else None)
df8

df8["longitude"] = df8["Coordinate"].apply(lambda x: x.longitude if x != None else None)
df8