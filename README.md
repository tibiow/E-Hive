# E-Hive
E-Hive c’est la solution connecté permettant de récupérer des informations sur la santé de la ruche jour après jour pour en voir l’évolution continue d’une ruche. On y trouve le poids en miel contenu dans la ruche ainsi que la population totale de cette dernière. Grâce aux mesures faites quotidiennement il est possible de mettre en place des corrélations avec la température ou d’autre facteur externe à la ruche.

## Installation

You need to run the following commands on both raspberry pi:

`/boot/config.txt:`

```
dtparam=spi=on

# i2c1
dtparam=i2c_arm=on
dtparam=i2c1=on

#i2c0?
dtparam=i2c_vc=on

#enable uart interface
enable_uart=1

#map mini-UART to internal bluetooth an free-up main UART to handle module
dtoverlay=pi3-miniuart-bt
```

## Run Application

You have 2 docker image. One is for embedded raspberry and the other is for the gateway.
Depending of which one you want to deploy you need to launch to good yml file with the command
```
docker-compose -f XXX.yml up
```

note : this command may not work. Because of nodered you can have permissions's issue on directories.
To solve this you can do a
```
chmod 777 data-application  data-embedded  data-gateway
```
