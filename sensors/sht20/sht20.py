import smbus
import time
import urllib.request
import json
import datetime
from sensor.SHT20 import SHT20

import smbus
import time

myurl = "http://nodered:1880/sensors"

def readTemperature(bus):
  sht = SHT20(bus, 0x40)
  t = sht.temperature()
  return t.C

def readHumidity(bus):
  sht = SHT20(bus, 0x40)
  h = sht.humidity()
  return h.RH

def sendTemp(bus):
  temperatureLevel=readTemperature(bus)
  humidityLevel = readHumidity(bus)
  print("Temperature" + str(bus) + " : " + format(temperatureLevel) + " lx")

  body = {'type': 'Temperature', 'sensorId': bus, 'value': temperatureLevel, 'date': datetime.datetime.now().isoformat()}

  req = urllib.request.Request(myurl)
  req.add_header('Content-Type', 'application/json; charset=utf-8')

  jsondata = json.dumps(body)
  jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
  req.add_header('Content-Length', len(jsondataasbytes))
  response = urllib.request.urlopen(req, jsondataasbytes)

  body = {'type': 'Humidity', 'sensorId': bus, 'value': humidityLevel, 'date': datetime.datetime.now().isoformat()}
  req = urllib.request.Request(myurl)
  req.add_header('Content-Type', 'application/json; charset=utf-8')

  jsondata = json.dumps(body)
  jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
  req.add_header('Content-Length', len(jsondataasbytes))
  response = urllib.request.urlopen(req, jsondataasbytes)


def main():

  while True:
    sendTemp(0)
    sendTemp(1)
    time.sleep(10)

if __name__=="__main__":
   main()
