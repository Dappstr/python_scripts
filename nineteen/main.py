import csv
import pandas

#with open("nineteen/weather_data.csv") as data_file:
    #data = data_file.readlines()
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
    
#    print(temperatures)

data = pandas.read_csv("nineteen/weather_data.csv")
temp_list = data["temp"].to_list()

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])