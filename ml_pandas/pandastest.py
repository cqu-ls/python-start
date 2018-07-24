import pandas

food_info = pandas.read_csv("../data/food_info.csv")
print(type(food_info))
print(food_info.dtypes)

print(food_info.head(3),food_info.tail(4))

print(food_info.columns)
print(food_info.shape)

print(food_info.loc[3:6])
print(food_info["Thiamin_(mg)"])
columns1 =["Thiamin_(mg)","Shrt_Desc"]
print(food_info[columns1])

clumns_names = food_info.columns.tolist()
print(clumns_names)
gram_columns =[x for x in clumns_names if x.endswith("(g)")]
print(gram_columns)
print(food_info[gram_columns])

print(food_info.shape)
iron_grams = food_info["Iron_(mg)"]/1000
food_info["Iron_(g)"] = iron_grams
print(food_info.shape)

iron_grams_max = food_info["Iron_(mg)"].max()


food_info.sort_index(by=["FA_Mono_(g)"],inplace=True,ascending=False)
print(food_info["FA_Mono_(g)"])
