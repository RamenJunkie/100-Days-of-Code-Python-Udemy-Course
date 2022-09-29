# Convert Large CSV of Data to a small CSV of Fur Colors and how many.
# grey, red (cinnamon), black
#file Squirrel_Count.csv

import pandas
file = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
data = pandas.read_csv(file)
colors_dict = {
    "Fur Color": ["Cinnamon", "Black", "Gray"],
    "Count": [],
}

for each in colors_dict["Fur Color"]:
    colors_dict["Count"].append(data["Primary Fur Color"].value_counts()[each])

#print(colors_dict)
my_panda = pandas.DataFrame(colors_dict)
my_panda.to_csv("Squirrel_Count.csv")