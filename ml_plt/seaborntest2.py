import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"distributions")))

x = np.random.normal(size=100)
xx = x.reshape(10,10)
print(xx.shape,x,stats.gamma)

sns.distplot(x,bins=20,kde=False,fit=stats.gamma)

mean,cov = [0,1],[(1,0.5),(0.5,1)]
data = np.random.multivariate_normal(mean,cov,100)
x,y = np.random.multivariate_normal(mean,cov,1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x,y=y,kind="hex",color="k")

df = pd.DataFrame(data,columns=["X","Y"])
sns.jointplot(x="X",y="Y",data=df)
plt.show()