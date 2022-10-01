import csv

cars = [] #the datas of one car
gps = []
distance = []

class Car:
    def __init__(self, t, axv, ayv, psidtopt, absreftime, vxv, vyv):
        self.t = t
        self.axv = axv
        self.ayv = ayv
        self.psidtopt = psidtopt #rotation
        self.absreftime = absreftime
        self.vxv = vxv
        self.vyv = vyv
class GPS:
    def __init__(self, t, Hunter_GPS_Mode):
        self.t = t
        self.Hunter_GPS_Mode = Hunter_GPS_Mode
class Distace:
    def __init__(self, t, Long_Delta_Distance, Long_Delta_Velocity):
        self.t = t
        self.Long_Delta_Distance = Long_Delta_Distance
        self.Long_Delta_Velocity = Long_Delta_Velocity

"""
Import of Group_416.csv
"""

with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv") as file416:
    csvfile = csv.reader(file416)
    next(csvfile)
    for row in csvfile:
        car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cars.append(car)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_416.csv") as file416:
    csvfile = csv.reader(file416)
    next(csvfile)
    for row in csvfile:
        car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cars.append(car)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_416.csv") as file416:
    csvfile = csv.reader(file416)
    next(csvfile)
    for row in csvfile:
        car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cars.append(car)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv") as file416:
    csvfile = csv.reader(file416)
    next(csvfile)
    for row in csvfile:
        car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cars.append(car)
'''
Import of Group_340.csv
'''
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_340.csv") as file340:
    csvfile = csv.reader(file340)
    next(csvfile)
    for row in csvfile:
        gps_data = GPS(row[0], row[1])
        gps.append(gps_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_340.csv") as file340:
    csvfile = csv.reader(file340)
    next(csvfile)
    for row in csvfile:
        gps_data = GPS(row[0], row[1])
        gps.append(gps_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_340.csv") as file340:
    csvfile = csv.reader(file340)
    next(csvfile)
    for row in csvfile:
        gps_data = GPS(row[0], row[1])
        gps.append(gps_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_340.csv") as file340:
    csvfile = csv.reader(file340)
    next(csvfile)
    for row in csvfile:
        gps_data = GPS(row[0], row[1])
        gps.append(gps_data)

'''
Import of Group_343.csv
'''

with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_343.csv") as file343:
    csvfile = csv.reader(file343)
    next(csvfile)
    for row in csvfile:
        distance_data = Distace(row[0], row[1], row[2])
        distance.append(distance_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_343.csv") as file343:
    csvfile = csv.reader(file343)
    next(csvfile)
    for row in csvfile:
        distance_data = Distace(row[0], row[1], row[2])
        distance.append(distance_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_343.csv") as file343:
    csvfile = csv.reader(file343)
    next(csvfile)
    for row in csvfile:
        distance_data = Distace(row[0], row[1], row[2])
        distance.append(distance_data)
with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_343.csv") as file343:
    csvfile = csv.reader(file343)
    next(csvfile)
    for row in csvfile:
        distance_data = Distace(row[0], row[1], row[2])
        distance.append(distance_data)