#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include "DHT.h" 

#define DHTPIN 5 //PIN 5   
#define DHTTYPE DHT11    //  DHT11 Sensor

DHT dht(DHTPIN, DHTTYPE); //Create Sensor as dht
 
const char* SSID = "WLAN-123456";
const char* PSK = "8200663485251411";
const char* MQTT_BROKER = "192.168.2.XXX";
const char* MQTT_PATH_Temp = "Sensor_Temperature";
const char* MQTT_PATH_Hum = "Sensor_Humidity"; 
const char* SENSOR_ID = "t_1";

 
WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {
    Serial.begin(115200);
    setup_wifi();
    client.setServer(MQTT_BROKER, 1883);
    dht.begin();
}
 
void setup_wifi() {
    delay(10);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID);
 
    WiFi.begin(SSID, PSK);
 
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
 
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}
 
void reconnect() {
    while (!client.connected()) {
        Serial.print("Reconnecting...");
        if (!client.connect("ESP8266Client")) {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" retrying in 5 seconds");
            delay(5000);
        }
    }
}
void loop() {

    delay(2000);
    if (!client.connected()) {
        reconnect(); //try reconnecting with WiFi
    }
    client.loop();
    
    float humidity = dht.readHumidity(); //get humidty data
  
    float temperature = dht.readTemperature();//get temperature data


      //Put Data in Json Format for Publishing
      StaticJsonDocument<200> temp;
      temp["t_1"] = temperature;

      StaticJsonDocument<200> humi;
      humi["t_1"] = humidity;
    
      char buffer1[256];
      serializeJson(temp, buffer1);
      char buffer2[256];
      serializeJson(humi, buffer2);
      //Publish
      client.publish(MQTT_PATH_Temp, buffer1);
      client.publish(MQTT_PATH_Hum,buffer2);   
              

    
}
