from cmps03 import *

compass = CMPS03()

compass.calibrate()
compass.changeScanTime(1)
compass.changeAdress(0)

print compass.softwareVersion()
print compass.bearing255()
print compass.bearing3599()