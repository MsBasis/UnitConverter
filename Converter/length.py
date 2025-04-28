#lenght conversions
#KM
#M
#CM
#MILES
#FOOT
#INCHES

NormalPeopleUnits = {
    "centimeters" : 100,
    "meters" : 1,
    "kilometers" : 0.001,
}

def metersConverter(unit,x):
    meter = unit * NormalPeopleUnits[f"{x}"]
    print(meter)

metersConverter(10,"kilometers")

