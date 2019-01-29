FROM nodered/node-red-docker:rpi-v8

VOLUME ["/data"]

USER root

RUN apt update && apt install wiringpi \
	&&  npm install node-red-contrib-lorawan

COPY . .

ENTRYPOINT ["./start-nodered.sh"]
