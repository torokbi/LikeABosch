import csv

cars = [] #the datas of one car

class Car:
    def __init__(self, t, axv, ayv, psidtopt, absreftime, vxv, vyv):
        self.t = t
        self.axv = axv
        self.ayv = ayv
        self.psidtopt = psidtopt #rotation
        self.absreftime = absreftime
        self.vxv = vxv
        self.vyv = vyv

with open("./SW Challenge 2022 - dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv") as file416:
    csvfile = csv.reader(file416)
    next(csvfile)
    for row in csvfile:
        car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cars.append(car)