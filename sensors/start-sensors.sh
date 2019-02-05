#!/bin/bash
python3 bh1750/bh1750.py &
python3 sht20/sht20.py &
python3 hx711/example.py &

# python3 scripts shouldn't exit, if they did quit the container, it'll be restart automatically
wait -n
killall python3
exit 1
