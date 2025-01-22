import pandas as pd
import csv

df = pd.read_csv("Pandas_trial/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250121.csv")

grey_data = df[df["Primary Fur Color"] == "Gray"]
black_data = df[df["Primary Fur Color"] == "Black"]
cinnamon_data = df[df["Primary Fur Color"] == "Cinnamon"]

# create a new csv with count of each color

new_data = {
    "Color": ["Gray", "Black", "Cinnamon"],
    "count": [len(grey_data), len(black_data), len(cinnamon_data)]
}

new = pd.DataFrame(new_data)
new.to_csv("Pandas_trial/data/color.csv")

