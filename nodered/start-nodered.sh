#!/bin/sh
gpio mode 4 OUT
gpio write 4 1
gpio readall

npm start -- --userDir /data
