#connects with MQTT Broker and waits for messages
import paho.mqtt.client as mqtt

#TOPICS
MQTT_PATH_TEMP = "Sensor_Temperature"
MQTT_PATH_HUM = "Sensor_Humidity"

#Callback - when PUBLISH message is received
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    #print received messages
    print("message received: ", msg)
    print("message topic: ", message.topic)
 
def on_connect(client, userdata, flags, rc):
    #Topic Subscriptions
    client.subscribe(MQTT_PATH_TEMP)
    client.subscribe(MQTT_PATH_HUM)

BROKER_ADDRESS = "localhost"
 
client = mqtt.Client() #Create instance of class client
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(BROKER_ADDRESS) #connect client to broker
 
print("Connected to MQTT Broker: " + BROKER_ADDRESS)
 
client.loop_forever()
