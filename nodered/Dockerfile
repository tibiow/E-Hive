FROM nodered/node-red-docker:rpi-v8

VOLUME ["/data"]

USER root

RUN apt update && apt install wiringpi \
	&&  npm install node-red-contrib-lorawan async # for some reason an older incomaptible version of async is used so install newer version manually

COPY . .

ENTRYPOINT ["./start-nodered.sh"]
