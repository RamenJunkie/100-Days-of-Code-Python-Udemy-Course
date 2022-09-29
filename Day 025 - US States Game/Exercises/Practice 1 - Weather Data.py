#with open("weather_data.csv", mode = "r") as weather_file:
#    data = weather_file.readlines()
#
#print(data)

#import csv
#
#with open("weather_data.csv", mode = "r") as weather_file:
#    data = csv.reader(weather_file)
#    temperatures = []
#    for row in data:
#        #print(row)
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#
#print(temperatures)
#print(f"Average Temperature: {sum(temperatures)/len(temperatures)}")

import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
#print(data["temp"])
#print(sum(data["temp"])/len(data["temp"]))
#print(type(data))
#print(type(data["temp"]))
#print(type(data["temp"][0]))
#print(type(data["day"][0]))

#print(data["temp"])
# Can Convert to various File types (Except Dictionary etc)



#data_dict = data.to_dict()
#print(data_dict)


#temps_list = data["temp"].to_list()

#print(temps_list)

#print(data['temp'].max())

#print(data.condition)

#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])


#Create a Data From from Scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_panda = pandas.DataFrame(data_dict)

print(my_panda)

my_panda.to_csv("my_new_data.csv")