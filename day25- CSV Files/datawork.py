import csv
import pandas
import math

#
# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #
# # print(data)
#
#
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for i in data: #i in this case is row number
# #         if i[1] != "temp":
# #             temperatures.append(int(i[1]))
# #
# #     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
#
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
#
# print(data_dict)
#
# data_list = data["temp"].to_list()
#
# print(data_list)
#
# #manually calculate mean
# ans = sum(data_list) / len(data_list)
# ans = "{:.2f}".format(ans)  #this formats to the hundreth (2 decimals) !!!rounded up!!!
# print(ans)
#
# mean = data["temp"].mean() #automatically get mean of data set
# max= data["temp"].max()
#
# print(mean)
# print(max)
#
# temperatures = data.temp
#
# print(temperatures)
#
# #get data in a row
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# print(monday.temp) #get mondays temp
# monday_temp_F = monday.temp * 1.8 + 32 #using this in an equation
#
# print(monday_temp_F)

#CREATE DATAFRAME FROM SCRATCH

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
fur_dict = data["Primary Fur Color"].to_dict()

gray_fur = 0
cin_fur = 0
black_fur = 0
nan_fur = 0
for index in fur_dict:
    if fur_dict[index] == "Gray":
        gray_fur+=1
    elif fur_dict[index] == "Cinnamon":
        cin_fur+=1
    elif fur_dict[index] == "Black":
        black_fur+=1
    else:
        nan_fur+=1


fur_data = {
     "Fur Color": ["Gray", "Cinnamon", "Black", "NaN"],
     "scores": [gray_fur,cin_fur,black_fur,nan_fur]
 }

fur_data_final = pandas.DataFrame(fur_data)
fur_data_final.to_csv("fur_data.csv")
