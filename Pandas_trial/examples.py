# import csv

# with open('Pandas_trial\data\weather_data.csv',mode='r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     temperature = []
#     # for row in csv_reader:
#     #     print(row)
#     for row in csv_reader:
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

df = pd.read_csv('Pandas_trial/data/weather_data.csv')
# print(df.head())

data_dict = df.to_dict()
# print(data_dict)

temp_list = df["temp"].to_list()
# print(data_list)

# find average of temp column
# print('average temperature is :', sum(temp_list)/len(temp_list))
# print('average temperature :', df["temp"].mean())

# # find maximum value of temp column
# print('max temperature is :', df["temp"].max())

# convert celsuis to farenhiet

# df['temp'] = (df['temp'] * (9/5)) +32
# print(df['temp'])

# create a dataframe and add it to csv

data = {
    "cities": ["Tokyo", "Paris", "New York"],
    "country": ["Japan", "France", "USA"]
}

df = pd.DataFrame(data)
print(data)
df.to_csv("data/new.csv")
