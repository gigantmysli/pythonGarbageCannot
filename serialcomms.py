import serial
import configparser
from easygui import enterbox
import os.path

mConfig = configparser.ConfigParser()
mSerialPortName = ""

#find serial port name in config file or get it from user
GetSPName()


print("Port Name: " + mSerialPortName)

exit


def GetSPName():
  if not os.path.exists("commsConfig.ini"):
    print("Config file not found")
    mConfigFile = open("commsConfig.ini","w",encoding="utf8")
    mSerialPortName = enterbox(msg = "Enter serial port name",title="Serial Interface Setup", default="COM1")
    mConfig['serial'] = {'portName': mSerialPortName}
    mConfig.write(mConfigFile)
    mConfigFile.close()
  else:
    mConfig.read("commsConfig.ini")
    mConfig.sections()
    mSerialPortName = ""
    if 'serial' in mConfig and 'portName' in mConfig['serial']:
      mSerialPortName = mConfig['serial']['portName']
    else:
      mSerialPortName = enterbox(msg = "Enter serial port name",title="Serial Interface Setup", default="COM1")
      mConfigFile = open("commsConfig.ini","w",encoding="utf8")
      mConfig['serial'] = {'portName': mSerialPortName}
      mConfig.write(mConfigFile)
      mConfigFile.close()