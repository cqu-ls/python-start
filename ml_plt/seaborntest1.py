import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

def simplot(flip=1):
    x = np.linspace(1,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)

#sns.set()
#simplot()
#plt.show()


plt.plot([0,1],[0,1],sns.xkcd_rgb["pale red"],lw=5)#xccd color
plt.plot([0,1],[0,2],sns.xkcd_rgb["medium green"],lw=4)
plt.plot([0,1],[0,3],sns.xkcd_rgb["denim blue"],lw=3)
plt.show()

sns.set_style("whitegrid")#dark white ticks
sns.set_context("paper",font_scale=2,rc={"lines:linewidth":1.5})
data = np.random.normal(size=(20,6))+np.arange(6)/2
#sns.boxplot(data=data,palette=sns.color_palette("hls",8))
sns.despine(left=False)
#simplot()
#plt.show()

#使用with域 显示不同的子图风格
with sns.axes_style("darkgrid"):
    plt.subplot(221)
    simplot()
with sns.axes_style("dark"):
    plt.subplot(222)
    simplot()

plt.subplot(223)
simplot(-1)

current_palette = sns.color_palette()#deep, muted, bright, pastel, dark, colorblind
#sns.palplot(current_palette)
#sns.palplot(sns.color_palette("hls",10))#自动分割rgb



