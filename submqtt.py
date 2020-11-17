import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import random
import time
import configparser
import json

def on_message(client,userdate,message):
  dados=json.loads(str(message.payload.decode()))
  if dados['field1'] != 0:
    print("musica tocando")
  else:
    print("sem música") #tentar fazer mp3 tocar =/

broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_SUBSCRIBE']
username=config['THINGSPEAK']['USERNAME']
password=config['THINGSPEAK']['MQTT_API_KEY']
subscribe.callback(on_message,qos=0,topics=topico,hostname=broker,port=port,client_id="clisub",auth={'username':username,'password':password})
while(True):
  time.sleep(10)