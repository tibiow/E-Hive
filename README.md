# E-Hive
E-Hive c’est la solution connecté permettant de récupérer des informations sur la santé de la ruche jour après jour pour en voir l’évolution continue d’une ruche. On y trouve le poids en miel contenu dans la ruche ainsi que la population totale de cette dernière. Grâce aux mesures faites quotidiennement il est possible de mettre en place des corrélations avec la température ou d’autre facteur externe à la ruche.

#installation

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

All of our script run with python and you need the latest python 3 on your embedded raspberri.
You also need to install these packages from pip

```
sudo pip3 install sensor
sudo pip3 install requests
sudo pip3 install HX711
sudo pip3 install RPi.GPIO
```

#Run Application


