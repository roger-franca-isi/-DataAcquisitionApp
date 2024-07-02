import json

class Sensor:
    def __init__(self, sensor_tag, sensor_implement, sensor_data, sensor_unit):
        self.sensor_tag = sensor_tag
        self.sensor_implement = sensor_implement
        self.sensor_data = sensor_data
        self.sensor_unit = sensor_unit
        self.topicMqtt = f"Projeto/{self.sensor_implement}/{self.sensor_tag}/uplink"
        
        print(f"Sensor Topic : {self.topicMqtt}")     

    def process_data_received(self, client, userdata, message):
        try:
            # Decodificar o payload JSON
            payload = json.loads(message.payload.decode('utf-8'))
            
            # Buscar a variável desejada (self.sensor_data)
            self.sensor_data_value = payload.get(self.sensor_data)
            
            if self.sensor_data_value is not None:
                self.callback_save_value(str(self.sensor_tag), float(self.sensor_data_value))
            else:
                print("Variável 'sensor_data' não encontrada no payload JSON.")
        
        except Exception as e:
            print(f"Erro ao processar mensagem: {e}")     
            
    def set_callback_save_value(self, callback):
        self.callback_save_value = callback
        

