import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate
import matplotlib as mpl


sns.set(color_codes=True)
#np.random.seed(sum(map(ord,"distributions")))
#np.random.seed(sum(map(ord,"regression")))
tips = sns.load_dataset("tips")
print(tips.head())
sns.regplot(x="total_bill",y="tip",data=tips)
sns.lmplot(x="size",y="tip",data=tips,x_jitter=0.5)
sns.stripplot(x="size",y="tip",data=tips)
#iris = sns.load_dataset("iris")
#sns.pairplot(iris)
plt.show()