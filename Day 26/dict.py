import pandas

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}

print(weather_f)

student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
for (index, row) in student_dataframe.iterrows():
    print(row.student)
