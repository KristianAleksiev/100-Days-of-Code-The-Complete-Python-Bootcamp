import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
number_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
number_cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
number_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(number_gray_squirrels)
print(number_black_squirrels)
print(number_cinnamon_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[number_gray_squirrels, number_cinnamon_squirrels, number_black_squirrels],
}
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrel_count.csv")