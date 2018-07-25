import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate
import matplotlib as mpl

sns.set(style="whitegrid",color_codes=True)
np.random.seed(sum(map(ord,"categorical")))

titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

#sns.stripplot(x="day",y="total_bill",data=tips,jitter=True)
sns.swarmplot(x="day",y="total_bill",hue="time",data=tips,alpha=0.5,color="r")
#sns.boxplot(x="day",y="total_bill",hue="time",data=tips)
sns.violinplot(x="day",y="total_bill",hue="sex",data=tips,split=True,alpha=0.5,color="b")
plt.show()
plt.close()

sns.barplot(x="sex",y="survived",hue="class",data=titanic)
print(type(titanic))
plt.show()
plt.close()

sns.pointplot(x="class",y="survived",hue="sex",data=titanic,palette={"male":"g","female":"m"},markers=["*","<"],linestyles=["--","-"])
plt.show()
plt.close()

sns.factorplot(x="time",y="total_bill",hue="smoker",col="day",row="sex",data=tips,kind="box")#kind:strip swarm box violin boxen point bar count
plt.show()