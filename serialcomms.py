import serial
import configparser
from easygui import enterbox



mConfig = configparser.ConfigParser()

text = enterbox(msg = "WOT THE FOK",title="FOK FOK", default="FOK DIFOT")

print(text)

mConfig['serial'] = {'portName': 'COM1'}


with open('commsConfig.ini', 'w') as configFile:
  mConfig.write(configFile)



mSr = serial.Serial()
mSr.port = "COM1"
