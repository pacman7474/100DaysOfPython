import csv
import pandas

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#   temperatures = []
#   for x,row in enumerate(data):
#       if x > 0:
#           temperatures.append(int(row[1]))
#    print(temperatures)

data = pandas.read_csv("weather_data.csv")


data_dict = data.to_dict()
temp_list = data["temp"].to_list()
total = 0

average = data["temp"].mean()
#print(average)

max = data["temp"].max()
#print(max)
#print(data.temp)

#Get Data in Row
print(data[data.day == "Monday"].temp * 9/5 + 32)

#Create a dataframe
data_dict2 = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data2 = pandas.DataFrame(data_dict2)
print(data2)
data2.to_csv("new_data.csv")