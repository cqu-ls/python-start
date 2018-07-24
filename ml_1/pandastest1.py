import numpy as np
import pandas as pd

titanic_survival = pd.read_csv("../data/titanic_train.csv")
print(titanic_survival.head())

age = titanic_survival["Age"]
age_is_null = pd.isnull(age)
age_null = age[age_is_null]
print(age_null)

mean_age = sum(titanic_survival["Age"][age_is_null==False])/len(titanic_survival["Age"][age_is_null==False])
print(mean_age,titanic_survival["Age"].mean())
#fillna 字典指定值填充指定列的NaN
age_fill_values ={'Age':titanic_survival["Age"].mean()}
#titanic_survival.fillna(value=age_fill_values,inplace=True)
print(age)

passager_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
print(passager_survival)
passager_age = titanic_survival.pivot_table(index="Pclass", values="Age")
print(passager_age,titanic_survival.pivot_table(index="Pclass", values="Age",aggfunc=np.mean))

port_status = titanic_survival.pivot_table(index="Embarked", values=["Fare","Survived"],aggfunc=np.sum)
print(port_status)
port_sum = titanic_survival.pivot_table(index=["Embarked","Pclass"],values="Fare",columns="Survived",aggfunc=np.sum)
#pivot_table中一个令人困惑的地方是“columns（列）”和“values（值）”的使用。记住，变量“columns（列）”是可选的，它提供一种额外的方法来分割你所关心的实际值。然而，聚合函数aggfunc最后是被应用到了变量“values”中你所列举的项目上
port_sum = titanic_survival.pivot_table(index=["Embarked","Pclass"],values="Fare",columns="Survived",aggfunc=[np.sum],fill_value=0,margins=True)
#非数值（NaN）有点令人分心。如果想移除它们，我们可以使用“fill_value”将其设置为0
print(port_sum)
print(titanic_survival["Age"])
#dropna 舍弃NaN
#new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age"])
#print(new_titanic_survival["Age"])

print(titanic_survival.loc[10,"Age"])

sort_titanic_by_age = titanic_survival.sort_values(by=["Age"],ascending=False)
print(sort_titanic_by_age)