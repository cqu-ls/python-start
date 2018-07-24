import numpy as np
import pandas as pd
from pandas import Series

fandango = pd.read_csv("../data/fandango_score_comparison.csv")
print(fandango.columns)

series_film=fandango["FILM"]
series_rt = fandango["RottenTomatoes"]
print(type(fandango),type(fandango["FILM"]),type(fandango[["FILM","RottenTomatoes"]]))

film_names = series_film.values
print(film_names,type(film_names))
print(series_rt[0:5])


rt_scores = series_rt.values
series_custom = Series(data=rt_scores,index=film_names)
print(series_custom,type(series_custom),series_custom.shape)
print(series_custom["Cinderella (2015)"])

fandango_film = fandango.set_index("FILM",drop=False)

print(fandango_film.index)
print("***********")
print(fandango_film.loc["Clouds of Sils Maria (2015)"])
print("-------")
print(fandango_film.loc[["Clouds of Sils Maria (2015)"]])

print((fandango["RottenTomatoes"]+fandango["Metacritic"])/2)