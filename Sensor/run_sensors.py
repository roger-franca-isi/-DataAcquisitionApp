from Sensor.sensor import Sensor
from Mqtt.mqtt_broker import MyMqtt
from typing import List

class SensorRun:
    def __init__(self, sensors :List[Sensor], mqtt_broker :MyMqtt, database_sensors):
        self.sensors = sensors
        self.mqtt_broker = mqtt_broker
        self.database_sensors = database_sensors
        
    def run(self):
        for sensor in self.sensors:
            self.mqtt_broker.subscribe(sensor.topicMqtt, self.process_sensor)

    def process_sensor(self):
        # Exemplo de processamento: imprimir informações do sensor
