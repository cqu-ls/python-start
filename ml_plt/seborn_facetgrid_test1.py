import numpy as np
import seaborn as sns
import pandas as pd
from pandas import Categorical
import matplotlib.pyplot as plt
from scipy import stats,integrate
import matplotlib as mpl


sns.set(color_codes=True)
np.random.seed(sum(map(ord,"axis_grids")))

tips = sns.load_dataset("tips")
flight = sns.load_dataset("flights")
print(tips.head(5))
print(flight.head(5))

g = sns.FacetGrid(tips,col="time",hue="smoker")
g.map(plt.scatter,"total_bill","tip")
g.add_legend()
plt.show()
plt.close()

order_days = tips.day.value_counts().index
print(order_days)
order_days = Categorical(["Thur","Fri","Sat","Sun"])
g = sns.FacetGrid(tips,col="day",col_order=order_days)
g.map(sns.boxplot,"total_bill")
plt.show()
plt.close()

pal = dict(Lunch="seagreen",Dinner="gray")
g = sns.FacetGrid(tips,hue="time",col="sex",row="smoker",palette=pal,size=5,hue_kws={"marker":["<",">"]})
g.map(plt.scatter,"total_bill","tip",s=50,alpha=0.7,linewidth=0.6,edgecolor="white")
g.add_legend()
g.fig.subplots_adjust(wspace=0.2,hspace=0.2)#子图之间的间距
#g.set_axis_labels("1","2")
#g.set(xticks=[10,30,50])
plt.show()

g = sns.PairGrid(tips,hue="smoker",vars=["total_bill","tip"],palette="GnBu_d")#vars指定对比的变量，自己选择
g.map_diag(plt.hist)#对角线
g.map_offdiag(plt.scatter)#非对角线
g.add_legend()
#g.map(plt.scatter)
plt.show()

flights = flight.pivot("month","year","passengers")
ax = sns.heatmap(flights,annot=True,fmt="d",linewidths="0.5",cmap="YlGnBu")
plt.show()

tip_corr = tips.corr()
sns.heatmap(tip_corr,annot=True,fmt="f",linewidths="0.5",cmap="YlGnBu")
plt.show()