#lenght conversions
#KM
#M
#CM
#MILE
#FEET
#INCHES
from constants import LenghtUnits


def metersConverter(unit,From,to):
    jednostka = unit * LenghtUnits[f"{From}"][f"{to}"]
    print(f"{jednostka} {to}" )

metersConverter(1500,"m","kilometer")

