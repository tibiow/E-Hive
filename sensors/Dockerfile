FROM debian:buster

USER root

RUN apt update && apt install -y python3 python3-smbus python3-rpi.gpio python3-numpy python3-pip psmisc \
	&& pip3 install sensor

COPY . .

ENTRYPOINT ["./start-sensors.sh"]
