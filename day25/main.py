# #with open("weather_data.csv", "r") as data:
# #    data_list = data.readlines()
# #    print(data_list)
#
#
# # import csv
# #
# # with open("weather_data.csv") as data:
# #     data_list = csv.reader(data)
# #     tempreture = []
# #     for row in data_list:
# #         print(row[1])
#
# import pandas
# #
# # # average = 0
# # data = pandas.read_csv("weather_data.csv")
# # data_temp = data["temp"].tolist()
# # # for d in range(len(data_temp) - 1):
# # #     average = average + data_temp[d] / len(data_temp)
# # #
# # # print(average)
# # # ave = sum(data_temp) / len(data_temp)
# # # print(ave)
# # # data_max = data["temp"].max()
# # print(data[data.temp == data.temp.max()])
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240603.csv")
# gray_fur = data[data["Primary Fur Color"] == "Gray"]
# print(len(gray_fur))
# black_fur = data[data["Primary Fur Color"] == "Black"]
# print(len(black_fur))
# cinnamon_fur = data[data["Primary Fur Color"] == "Cinnamon"]
# print(len(cinnamon_fur))
#

# data_dic = {
#     "Fur Color": ["Cinnamon", "Black", "Gray"],
#     "Numbers": [cinnamon_fur, black_fur, gray_fur]
# }
#
# df = pandas.DataFrame(data_dic)
# df.to_csv("color.csv")
#
from turtle import Turtle, Screen
import pandas


screen = Screen()
states = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
states.shape(image)
answer = screen.textinput(title="Guss the state", prompt="states name")
answer_title = answer.lower()

states50 = pandas.read_csv("50_states.csv")
list_states = states50["state"]
if list_states.lower() == answer_title:
    print(answer_title)


screen.mainloop()



















