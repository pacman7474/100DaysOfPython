import pandas

#how many squirrels of each color
squirrel_raw = pandas.read_csv("Central_Park_Squirrel_Census.csv")
colors = squirrel_raw["Primary Fur Color"].unique()
color_count = squirrel_raw.groupby(['Primary Fur Color']).size()

print(color_count)
color_count.to_csv("squirrel_count.csv")