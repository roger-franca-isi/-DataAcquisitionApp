from Sensor.sensor import Sensor

class SensorRun:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        # Adiciona um sensor à lista de sensores
        self.sensors.append(sensor)
        
    def set_data_storage_callback(self, callback):
        self.storage_callback = callback

    def set_mqtt_subscribe_callback(self, callback):
        self.subscribe_callback = callback

    def set_mqtt_unsubscribe_callback(self, callback):
        self.unsubscribe_callback = callback
        
    def run(self):
        for sensor in self.sensors:
            callback_instance = self.storage_callback
            sensor.set_callback_save_value(callback_instance)
            self.subscribe_callback(sensor.topicMqtt, sensor.process_data_received)

    def stop(self):
        for sensor in self.sensors:
            self.unsubscribe_callback(sensor.topicMqtt)
