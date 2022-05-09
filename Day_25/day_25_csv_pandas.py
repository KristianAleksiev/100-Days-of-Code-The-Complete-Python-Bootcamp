### Day 25 - Working with CSV Files and Analysing Data with Pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"]) #Series type

data_dictionary = data.to_dict() #Every column becoming a key
print(data_dictionary)

temp_list = data["temp"].to_list() #Turns the "temp" series into a list
average_t = sum(temp_list) / len(temp_list) #Average temperature, mean
data["temp"].mean()
data["temp"].max()

data.condition #=> selecting the columns directly, key, data in columns

###Getting the data from a row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) #Getting the row with the max temp


monday = data[data.day == "Monday"]
print(monday.condition) #=> Sunny

####

monday_temp = int(monday.temp)
monday_temp_fahrenheit = monday_temp *9/5 + 32
print(monday_temp_fahrenheit)

### How to create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Kristian"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict) #Positional arguments
data.to_csv("new_data.csv") #Creating a new csv in the current directory