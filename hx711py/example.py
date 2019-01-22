import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

hx1 = HX711(5, 26)
hx2 = HX711(6, 26)
hx3 = HX711(13, 26)

# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it change.
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx1.set_reading_format("LSB", "MSB")
hx2.set_reading_format("LSB", "MSB")
hx3.set_reading_format("LSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
hx1.set_reference_unit(92)

hx1.reset()
hx1.tare()


hx2.set_reference_unit(92)

hx2.reset()
hx2.tare()


hx3.set_reference_unit(92)

hx3.reset()
hx3.tare()

import urllib.request
import json
import datetime

myurl = "http://raspberrymiaou.local:1880/sensors"

def sendValue(val, sid):
    body = {'type': 'Weight', 'sensorId': sid, 'value': val, 'date': datetime.datetime.now().isoformat()}

    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)


while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment the three lines to see what it prints.
        #np_arr8_string = hx.get_np_arr8_string()
        #binary_string = hx.get_binary_string()
        #print binary_string + " " + np_arr8_string
        
        # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
        val1 = hx1.get_weight(5)
        val2 = hx2.get_weight(5)
        val3 = hx3.get_weight(5)
        print(val1)
        print(val2)
        print(val3)
        print("--------")

        sendValue(val1, 1)
        sendValue(val2, 2)
        sendValue(val3, 3)


        hx1.power_down()
        hx1.power_up()
        hx2.power_down()
        hx2.power_up()
        hx3.power_down()
        hx3.power_up()

        time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
