# MQTT_Exchange_RaspberryPi

Scripts for a small IoT-Network:


- Receive data from a temperatur sensor and publish it via MQTT network protocol

-> Temperatur_Sensor_Publisher.py (e.g. Raspberry Pi)
-> ESP_Microcontroller_Publisher (e.g. ESP8266)

- Subscribe sensor data and insert it to Database

-> MQTT_Broker.py   (Create Broker, Subscribe to sensor data topics)
-> DB_functions.py  (Functions for connecting to the database as well as fetching/inserting Data)

- Displaying Sensordata in a table

-> Display_Data (.php) (Fetching Sensor Data from the Database, simple basic display)
