# -*- coding: utf-8 -*-
#connects with MQTT Broker and waits for messages
import paho.mqtt.client as mqtt
import time
import DB_functions as db
from datetime import datetime
import json

MQTT_PATH_Temp = "Sensor_Temperature" #Channel
MQTT_PATH_Hum = "Sensor_Humidity" #Channel
BROKER_ADDRESS = "localhost"

Messages = [] #array for saving the sensor messages
#Callback - when PUBLISH message is received
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received: ", msg)
    print("message topic: ", message.topic)
    Messages.append(msg)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker " + BROKER_ADDRESS )
    else:
        print("Failed to connect, return code %d\n", rc)
    #Subscribe topic
    client.subscribe(MQTT_PATH_Temp)
    client.subscribe(MQTT_PATH_Hum)

def run():
    client = mqtt.Client() #Create instance of class client
    print(client)
    #Callbacks
    client.on_connect = on_connect  #if connected to broker -> start
    client.on_message = on_message
     
    client.connect(BROKER_ADDRESS) #connect client to broker
     
    print("Connected to MQTT Broker: "+ BROKER_ADDRESS)
    client.loop_start()
    #Process received messages
    while True:
        if len(Messages) > 0:
            #get current timesatmp
            now = datetime.now()
            date = now.strftime('%Y-%m-%d')
            timestamp = now.strftime('%H:%M:%S')
            #get json data
            Dict_Humidity = json.loads(Messages[1])
            Dict_Temperature= json.loads(Messages[0])
            print(type(Dict_Humidity))
            DictValue_T = Dict_Humidity.values()
            DictValue_H = Dict_Temperature.values()
            DictKeys_T = Dict_Humidity.keys()
            DictKeys_H = Dict_Temperature.keys()
            temperature = float([x for x in DictValue_T][0])
            humidity = float([x for x in DictValue_H][0])
            sensor_id = str([x for x in DictKeys_H][0])
            #insert to database
            db.insert_data_temperatureTable(date,timestamp, sensor_id, temperature, humidity)
            Messages.clear()
            
    client.disconnect()
    client.loop_stop()

if __name__ == '__main__':
    run()
