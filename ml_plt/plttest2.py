import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

reviews = pd.read_csv("../data/fandango_scores.csv")
#print(reviews.columns)

cols = ['Fandango_Stars', 'Fandango_Ratingvalue',
       'RT_norm', 'RT_user_norm','IMDB_norm','Metacritic_user_nom']

norm_reviews = reviews[cols]
print(norm_reviews)

bar_height = norm_reviews.ix[0,cols].values
print(bar_height)
bar_position = np.arange(6)+0.5
print(bar_position)

fig,ax = plt.subplots()
ax.bar(bar_position,bar_height,0.5)
ax.scatter(np.arange(5),np.arange(5))
plt.show()