#!/bin/sh
python3 bh1750/bh1750.py &
python3 sht20/sht20.py &
python3 hx711/example.py
