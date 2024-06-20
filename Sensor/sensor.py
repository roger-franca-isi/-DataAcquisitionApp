class Sensor:
    def __init__(self, sensor_tag, sensor_implement, sensor_data1, sensor_unit1):
        self.sensor_tag = sensor_tag
        self.sensor_implement = sensor_implement
        self.sensor_data1 = sensor_data1
        self.sensor_unit1 = sensor_unit1
        self.topicMqtt = f"Projeto/{self.sensor_implement}/{self.sensor_tag}"

