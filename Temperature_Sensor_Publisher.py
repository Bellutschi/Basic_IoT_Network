import Adafruit_DHT #library for aquiring sensor data
import paho.mqtt.publish as publish #publish module
#CONSTANTS
MQTT_SERVER = "XXX.XXX.XXX.XXX"    #IP of Broker
#TOPICS
MQTT_TOPIC_TEMP = "Sensor1/Temperature"
MQTT_TOPIC_HUM = "Sensor1/Humidity"
PIN = 4

#infinite loop
while True:
    #get sensor data
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
    #publish sensor data
    publish.single(MQTT_TOPIC_TEMP, humidity, hostname=MQTT_SERVER)
    publish.single(MQTT_TOPIC_HUM, temperature, hostname=MQTT_SERVER)

    
