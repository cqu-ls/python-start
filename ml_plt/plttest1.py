import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("../data/unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate)

first_twelve = unrate[0:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Values")
plt.title("title")
plt.legend(loc="best")
plt.show()

fig = plt.figure()

ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,4)
ax3 = fig.add_subplot(2,3,6)
ax1.plot(first_twelve["DATE"],first_twelve["VALUE"])
ax2.plot(first_twelve["DATE"],first_twelve["VALUE"])
ax3.plot(first_twelve["DATE"],first_twelve["VALUE"])
plt.legend(loc="best")
plt.xticks(rotation=45)
plt.show()