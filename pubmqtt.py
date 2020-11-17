import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser
broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_PUBLISH']
mov_geladeira=0
while(True):
  mov_geladeira=random.randint(0,1)
  dados="field1={}&status=NQTTPUBLISH".format(mov_geladeira)
  publish.single(payload=dados,topic=topico,port=port,hostname=broker)
  print(dados)
  time.sleep(10)